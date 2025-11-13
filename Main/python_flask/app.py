from flask import Flask, request, redirect

app = Flask(__name__)

# Simple list to store todos (in memory)
todos = []

@app.route('/')
def home():
    # Simple HTML as string - no templates needed
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple Todo App</title>
        <style>
            body { font-family: Arial; margin: 40px; }
            .container { max-width: 600px; margin: 0 auto; }
            h1 { color: #333; }
            form { margin-bottom: 20px; }
            input[type="text"] { padding: 10px; width: 300px; }
            button { padding: 10px 15px; background: #28a745; color: white; border: none; cursor: pointer; }
            .todo-item { background: #f8f9fa; padding: 10px; margin: 5px 0; border-left: 4px solid #007bff; }
            .completed { text-decoration: line-through; color: #6c757d; border-left-color: #6c757d; }
            .actions { margin-top: 5px; }
            .actions a { margin-right: 10px; padding: 5px 10px; text-decoration: none; border-radius: 3px; }
            .complete { background: #007bff; color: white; }
            .delete { background: #dc3545; color: white; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>✅ Simple Todo App</h1>
            
            <form method="POST" action="/add">
                <input type="text" name="task" placeholder="Enter a new task" required>
                <button type="submit">Add Task</button>
            </form>
            
            <h3>Your Tasks:</h3>
    """
    
    # Add todos to HTML
    if not todos:
        html += "<p>No tasks yet. Add your first task above!</p>"
    else:
        for i, todo in enumerate(todos):
            status = "completed" if todo['done'] else ""
            html += f"""
            <div class="todo-item {status}">
                <div>{todo['task']}</div>
                <div class="actions">
                    <a class="complete" href="/toggle/{i}">{"Undo" if todo['done'] else "Complete"}</a>
                    <a class="delete" href="/delete/{i}">Delete</a>
                </div>
            </div>
            """
    
    html += """
        </div>
    </body>
    </html>
    """
    return html

@app.route('/add', methods=['POST'])
def add_todo():
    task = request.form.get('task')
    if task:
        todos.append({'task': task, 'done': False})
    return redirect('/')

@app.route('/toggle/<int:index>')
def toggle_todo(index):
    if 0 <= index < len(todos):
        todos[index]['done'] = not todos[index]['done']
    return redirect('/')

@app.route('/delete/<int:index>')
def delete_todo(index):
    if 0 <= index < len(todos):
        todos.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)