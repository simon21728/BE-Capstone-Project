from django.db import models
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

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
    if value <= timezone.now().date():
        raise ValidationError('Due date must be in the future.')

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField(validators=[validate_due_date])
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.title
