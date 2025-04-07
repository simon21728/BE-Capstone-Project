

 # Django Project:
 # Title: BE Capstone Project – Task Management API
First, let's create the project structure and install the necessary dependencies:
## Create a new Django project:

bash
django-admin startproject task_manager
cd task_manager
## Create a new app to handle task management:
bash
python manage.py startapp tasks
## Install dependencies: I’ll need to install Django and Django REST Framework:
bash
pip install django djangorestframework
## Add the app and DRF to my INSTALLED_APPS in settings.py:
python
INSTALLED_APPS = [
    # other apps...
    'rest_framework',
    'tasks',
]
## Run Migrations:
To create the database tables for these models:
bash
python manage.py makemigrations
python manage.py migrate
## Authentication
### User Registration & Login:
                          :User Registration View: 
                         :serializers.py to handle user creation
### User Login (JWT): Use djangorestframework-simplejwt for JWT token-based authentication.
## Install JWT:pip install djangorestframework-simplejwt
## Update settings.py to add JWT configuration:

# Models
Define models for each of the features mentioned. I’ll break down the models and their relationships.
User (Django User model):
   I can use Django’s built-in User model to handle user authentication.
 ## Task Model:
   A task will contain details like title, description, status, due date, and other fields relevant to tasks.
## Project Model:
   A project is a container for tasks and can have fields like name, description, start and end dates.
## Tag Model:
   Tags help categorize tasks. A task can have multiple tags, and a tag can be associated with multiple tasks.
## TaskTag Model:
   This is a many-to-many relationship model that connects tasks with tags.
## Comment Model:
   Users can comment on tasks to discuss details or updates.
## TaskHistory Model:
   Tracks the changes made to the task (e.g., status updates, changes to title or description).

# Project Commits Summary:
## Commit 1: Basic API Structure
   ### Set up foundational architecture for Task Management API
   ### Established Django project with REST framework
   ### Created initial models and serializers
## Commit 2: Users Management (CRUD)
   ### Implemented complete user lifecycle operations:
   ### User registration endpoint
   ### Profile management (read/update)
   ### Account deletion
   ### Added JWT authentication system
   ### Configured permission classes for user isolation

## Commit 3: Endpoint Minimization with ViewSets
   ### Migrated from APIView to ModelViewSet for:
   ### Reduced endpoint declarations
   ### Automatic CRUD routing
   ### Consistent behavior patterns
   ### Achieved 75% reduction in view code
## Commit 4: user with ForeignKey
## Commit 5:Add other model, i.e projects, tags, task-tags,comments,task-history and ajest README.md files

#  Current Technical Implementation:
# ViewSet Transition:
  ##  Replaced multiple APIView classes with:
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
   ## Router configuration:
      router = DefaultRouter()
      router.register(r'tasks', TaskViewSet)
       router.register(r'users', UserViewSet)

# Functional Requirements Status:
 ## 1.Task Management (CRUD)
   ### Fully implemented with ViewSets
   ### Attributes handled:
          ✔️Title (CharField)
          ✔️Description (TextField)
          ✔️Due Date (DateField with future validation)
          ✔️Priority (ChoiceField: Low/Medium/High)
          ✔️Status (ChoiceField: Pending/Completed)
   ### Validations:
           def validate_due_date(self, value):
               if value < timezone.now().date():
               raise serializers.ValidationError("Due date must be in the future")
               return value
  ## 2. Users Management (CRUD)  
       Complete implementation  
       Unique constraints:   

# Critical Bug Resolution:
## Error Encountered:
  ```python
  TypeError: Field 'id' expected a number but got datetime.datetime
  ```
## Root Cause:
   ### Database schema mismatch during model evolution
   ### Incorrect type assignment in migration sequence

## Solution Implemented:
   ###   1.Reset database schema:
       ```python
       rm db.sqlite3
       find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
       ```
   ### 2.Modified user relation in Task model:
        ```python
         user = models.ForeignKey(
          User, 
          on_delete=models.CASCADE,
          related_name='tasks',
          null=True,  # Temporary allowance
          blank=True
           )
        ```

# Current System Status:
  ## All CRUD operations functional
  ## Proper user isolation implemented
  ## Optimized endpoint structure via ViewSets
  ## Data validation working as expected
  ## Authentication system fully operational

# Next Steps:
 ## Implement automated testing
 ## Add filtering/sorting capabilities
 ## Set up pagination for task lists
 ## Develop comprehensive documentation (Swagger/Redoc)
       

     
