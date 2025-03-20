from django.urls import path
from . import views
from .views import TaskCreateAPIView,TaskListAPIView, TaskDetailAPIView,TaskUpdateAPIView,TaskDeleteAPIView
from .views import LogoutView,LoginAPIView
from rest_framework_simplejwt import views as jwt_views
from .views import CustomTokenObtainPairView,UserRegistrationView

urlpatterns = [
     # User Endpoints
    path('users/create/', views.UserCreateAPIView.as_view(), name='user-create'),
    path('users/', views.UserListAPIView.as_view(), name='user-list'),
    path('users/<int:user_id>/', views.UserDetailAPIView.as_view(), name='user-detail'),
    path('users/<int:user_id>/update/', views.UserUpdateAPIView.as_view(), name='user-update'),
    path('users/<int:user_id>/delete/', views.UserDeleteAPIView.as_view(), name='user-delete'),


    path('tasks/create/', TaskCreateAPIView.as_view(), name='task-create'),
    path('tasks/', TaskListAPIView.as_view(), name='task-list'),
    path('tasks/<int:task_id>/', TaskDetailAPIView.as_view(), name='task-detail'),
    path('tasks/<int:task_id>/update/', TaskUpdateAPIView.as_view(), name='task-update'),
    path('tasks/<int:task_id>/delete/', TaskDeleteAPIView.as_view(), name='task-delete'),
    
    # JWT Token Endpoints
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    path('api/login/', LoginAPIView.as_view(), name='token_obtain_pair'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
]