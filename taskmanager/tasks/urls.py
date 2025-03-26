from django.urls import path
from . import views
from .views import TaskViewSet,UserViewSet ,ProjectViewSet, TagViewSet,TaskTagViewSet, CommentViewSet, TaskHistoryViewSet
from .views import LogoutView,LoginAPIView
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter
from .views import CustomTokenObtainPairView,UserRegistrationView

# Create a router to automatically register the ViewSets
router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tags', TagViewSet)
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'task-tags', TaskTagViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'task-history', TaskHistoryViewSet)

urlpatterns = [
    # Auth and Registration Views
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserRegistrationView.as_view(), name='register'),

    # JWT token view
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),

] + router.urls
