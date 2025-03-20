from django.urls import path
from .views import TaskCreateAPIView,TaskListAPIView, TaskDetailAPIView,TaskUpdateAPIView,TaskDeleteAPIView


urlpatterns = [
    path('tasks/create/', TaskCreateAPIView.as_view(), name='task-create'),
    path('tasks/', TaskListAPIView.as_view(), name='task-list'),
    path('tasks/<int:task_id>/', TaskDetailAPIView.as_view(), name='task-detail'),
    path('tasks/<int:task_id>/update/', TaskUpdateAPIView.as_view(), name='task-update'),
    path('tasks/<int:task_id>/delete/', TaskDeleteAPIView.as_view(), name='task-delete'),
]