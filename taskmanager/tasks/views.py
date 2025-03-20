from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404

# 
class TaskCreateAPIView(APIView):
    def post(self, request):
        print("Request Data:", request.data)  # Debugging line
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("Serializer Errors:", serializer.errors)  # Debugging line
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskListAPIView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

class TaskDetailAPIView(APIView):
    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

class TaskUpdateAPIView(APIView):
    def put(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        if task.status == 'Completed' and request.data.get('status') != 'Pending':
            return Response(
                {"error": "Cannot change status of a completed task."},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDeleteAPIView(APIView):
    def delete(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)