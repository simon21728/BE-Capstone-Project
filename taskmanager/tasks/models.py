from django.db import models
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

# Priority choices for tasks
PRIORITY_CHOICES = [
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
]

# Status choices for tasks
STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Completed', 'Completed'),
]

def validate_due_date(value):
    """Ensure that the due date is in the future."""
    if value <= timezone.now().date():  # `timezone.now().date()` gives only the date (no time)
        raise ValidationError('Due date must be in the future.')


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField(null=True,blank=True)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name   
    
class TaskTag(models.Model):
    task = models.ForeignKey(Task, related_name='tags', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.task.title} - {self.tag.name}'
class Comment(models.Model):
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.task.title}'
    
class TaskHistory(models.Model):
    task = models.ForeignKey(Task, related_name='history', on_delete=models.CASCADE)
    change_description = models.TextField()
    changed_by = models.ForeignKey(User, related_name='task_changes', on_delete=models.CASCADE)
    changed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Change on {self.task.title} by {self.changed_by.username}'   