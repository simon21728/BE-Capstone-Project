from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

    
class CustomTokenObtainPairSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = User.objects.filter(username=attrs['username']).first()
        if user and user.check_password(attrs['password']):
            if not user.is_active:
                raise serializers.ValidationError("User is not active")
        else:
            raise serializers.ValidationError("Invalid username or password")
        return super().validate(attrs)
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class TaskSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Task
        fields = '__all__'  # or you can list specific fields like ['id', 'title', 'description', 'completed']
