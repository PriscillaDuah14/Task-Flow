# Task-Flow
A simple Flask-based API that allows users to manage tasks. Each task includes a title, description, done status, and a due date.

## Table of Contents
Installation
Running the Application
API Endpoints
Create Task
Get All Tasks
Get Task by ID
Update Task
Delete Task
Error Handling
Testing the API


## Installation

Clone this repository:

git clone https://github.com/your-username/task-api.git
Navigate to the project directory:


cd Taskflow-Backend
Create a virtual environment (optional but recommended):

python3 -m venv venv
Activate the virtual environment:

On Windows:
venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate

# Install the required dependencies:

pip install -r requirements.txt
Install Flask if it's not already in your requirements.txt:
We added the format in this file,

pip install flask

# Running the Application
Once everything is installed, you can run the application with:

python app.py
The server will start, and you can access the API at http://127.0.0.1:5000/.

## API Endpoints
1. Create Task
Endpoint: POST /api/tasks

Description: Creates a new task with a title, description, done status, and due date.

Request Body (JSON):
{
  "title": "Finish homework",
  "description": "Complete all assignments before the deadline",
  "done": false,
  "due_date": "2025-01-20"
}
Response (JSON):

{
  "id": 3,
  "title": "Finish homework",
  "done": false,
  "description": "Complete all assignments before the deadline",
  "due_date": "2025-01-20"
}
# Response Codes:

201 Created: Task created successfully.
400 Bad Request: Missing required fields or invalid data format.

2. Get All Tasks
Endpoint: GET /api/tasks

Description: Retrieves a list of all tasks.

Response (JSON):


  {
    "id": 1,
    "title": "Do laundry",
    "done": false,
    "description": "Wash clothes and dry them",
    "due_date": "2025-01-15"
  },
  {
    "id": 2,
    "title": "Buy groceries",
    "done": true,
    "description": "Get ingredients for the week",
    "due_date": "2025-01-10"
  }

# Response Codes:

200 OK: List of tasks returned successfully.

3. Get Task by ID
Endpoint: GET /api/tasks/{task_id}

Description: Retrieves a specific task by its ID.

Example: GET /api/tasks/1

Response (JSON):


{
  "id": 1,
  "title": "Do laundry",
  "done": false,
  "description": "Wash clothes and dry them",
  "due_date": "2025-01-15"
}
# Response Codes:

200 OK: Task found and returned.
404 Not Found: Task not found.

4. Update Task
Endpoint: PUT /api/tasks/{task_id}

Description: Updates an existing task's title, description, done status, or due date.

Request Body (JSON):

{
  "title": "Do laundry and fold clothes",
  "done": true,
  "description": "Wash clothes, dry them, and fold the clean clothes",
  "due_date": "2025-01-17"
}
Response (JSON):

{
  "id": 1,
  "title": "Do laundry and fold clothes",
  "done": true,
  "description": "Wash clothes, dry them, and fold the clean clothes",
  "due_date": "2025-01-17"
}
# Response Codes:

200 OK: Task updated successfully.
400 Bad Request: Invalid data format or missing fields.
404 Not Found: Task with specified ID does not exist.

5. Delete Task
Endpoint: DELETE /api/tasks/{task_id}

Description: Deletes a task by its ID.

Example: DELETE /api/tasks/1

Response (JSON):

{
  "message": "Task deleted successfully"
}
# Response Codes:

200 OK: Task deleted successfully.
404 Not Found: Task with specified ID does not exist.

## Error Handling
400 Bad Request: If the required fields (title, description, due_date) are missing or have invalid data formats (e.g., invalid due_date format), the API will respond with a 400 status code and a detailed error message.
404 Not Found: If the task ID provided does not exist when querying or attempting to update/delete, the API will return a 404 error.
Example error response for invalid due_date format:

{
  "error": "Invalid date format. Please use YYYY-MM-DD."
}


## Testing the API
You can use Thunder Client (VS Code Extension) or Postman to test the API. Follow these steps:

Install Thunder Client from the VS Code Extensions Marketplace.
Use the following requests to test the API:
POST /api/tasks to create a task.
GET /api/tasks to retrieve all tasks.
GET /api/tasks/{id} to retrieve a specific task.
PUT /api/tasks/{id} to update a task.
DELETE /api/tasks/{id} to delete a task.
Example Thunder Client Workspace
You can create a Thunder Client Workspace for organizing your API requests. It will include requests for:

Create Task (POST)
Get All Tasks (GET)
Get Task by ID (GET)
Update Task (PUT)
Delete Task (DELETE)


## Project Structure

askflow-backend/
├── app/
│   ├── models.py          # Contains the sql structure
│   ├── routes.py          # Contains the app codes
│   ├── config.py          # Mysql connections and configurations
├── migrations/            # Migrations files just in case
├── run.py                 # A sample of the app
├── requirements.txt       # Formats and installation guidelines
├── README.md---- Project documentation


## Future Enhancements

Implement a frontend using React or Angular for better user interaction.

Add user authentication and authorization for secure access.

Integrate with data visualization libraries to display graphical summaries.

Expand the reporting feature to include year-to-date summaries and savings goals.

## Contributors

- Priscilla Duah
[LinkedIn](http://linkedin.com/in/priscilla-antwiwaa-duah-7485b532a)

- Dorgbetor Catherena Emefa
[Github](https://github.com/dorgbetorcatherena) 

Feel free to reach out for questions or contribution

