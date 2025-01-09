# app.py
from flask import Flask, jsonify, request, abort
from datetime import datetime

import config
from dotenv import load_dotenv
import os

# Load environment variables from .env file (optional)
load_dotenv()

# Create Flask app instance
app = Flask(__name__)

# Apply the configuration settings
app.config.from_object('config')

# Sample data (could be replaced with a database later)
tasks = [
    {'id': 1, 'title': 'Do laundry', 'done': False,'description': 'Wash clothes and dry them', 'due_date': '2025-01-15'},
    {'id': 2, 'title': 'Buy groceries', 'done': False,'description': 'Get ingredients for the week', 'due_date': '2025-01-10'}

]

# Utility function to find task by ID
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        abort(404, description="Task not found")
    return task

# Route to create a new task
@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()

    if not data or 'title' not in data or 'description' not in data or 'due_date' not in data:
        abort(400, description="Title, description, and due_date are required")

    try:
        # Validate due_date format (YYYY-MM-DD)
        due_date = datetime.strptime(data['due_date'], '%Y-%m-%d')
    except ValueError:
        abort(400, description="Invalid date format. Please use YYYY-MM-DD.")

    task_id = len(tasks) + 1
    new_task = {
        'id': task_id,
        'title': data['title'],
        'done': data.get('done', False),
        'description': data['description'],
        'due_date': due_date.strftime('%Y-%m-%d')  # store the date in YYYY-MM-DD format
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# Route to get all tasks
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Route to get a specific task by id
@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_single_task(task_id):
    task = get_task(task_id)
    return jsonify(task)

# Route to update an existing task
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = get_task(task_id)
    data = request.get_json()

    if 'title' in data:
        task['title'] = data['title']
    if 'done' in data:
        task['done'] = data['done']
    if 'description' in data:
        task['description'] = data['description']
    if 'due_date' in data:
        try:
            due_date = datetime.strptime(data['due_date'], '%Y-%m-%d')
            task['due_date'] = due_date.strftime('%Y-%m-%d')
        except ValueError:
            abort(400, description="Invalid date format. Please use YYYY-MM-DD.")
    
    return jsonify(task)

# Route to delete a task
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = get_task(task_id)
    tasks.remove(task)
    return jsonify({"message": "Task deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)