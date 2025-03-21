commits:
        1 basic structure for an API Task Management project
        2. Users Management (CRUD)
        3 minimization of end point using ViewSet
                              
  I am currently utilizing APIView; however, the end points are becoming increasingly frequent. Consequently, I am interested in transitioning to ViewSet. Django Rest Framework's ModelViewSet and ViewSet classes can be utilized to achieve this. 


       Functional Requirements:
1.Task Management (CRUD):
Implement the ability to Create, Read, Update, and Delete (CRUD) tasks.
Each task should have the following attributes: Title, Description, Due Date, Priority Level (e.g., Low, Medium, High), and Status (e.g., Pending, Completed).
Ensure validations such as a due date in the future, priority level restrictions, and proper status updates.
2.Users Management (CRUD):
Implement CRUD operations for users.
A user should have a unique Username, Email, and Password.
Ensure that each user can manage their own tasks and has no access to tasks of other users. 


