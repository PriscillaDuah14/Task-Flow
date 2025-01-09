from flask import Flask, jsonify,request,abort

app = Flask(__name__)


tasks = [
    {'id': 1, 'title': 'Do laundry', 'done': False},
    {'id': 2, 'title': 'Buy groceries', 'done': False}
]

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": ["task1", "task2", "task3"]})



# Route to create a new task
@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'title' not in data:
        abort(400, description="Title is required")
    
    task_id = len(tasks) + 1
    new_task = {
        'id': task_id,
        'title': data['title'],
        'done': False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201



# Route to update an existing task
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = get_task(task_id)
    data = request.get_json()

    # Update fields if provided in the request body
    if 'title' in data:
        task['title'] = data['title']
    if 'done' in data:
        task['done'] = data['done']
    
    return jsonify(task)


if __name__ == '__main__':
    app.run(debug=True)

