import socket
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone


app = Flask(__name__)

# Telling app where the databasae is located, /// for relative path, //// for absolute path, test.db is the database name, everything will be stored in it
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# Initialize database
db = SQLAlchemy(app)

# Create a model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    # Every time we make a new element, this will return the task and its unique id
    def __repr__(self):
        return '<Task %r>' % self.id

# Index route for the app
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']

        # ✅ prevent empty or whitespace-only tasks
        if not task_content.strip():
            return redirect('/')

        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)
    

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting that task"


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue updating your task"
    else:
        return render_template('update.html', task=task)


if __name__ == "__main__":

    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    app.run(debug=True)

    # print(f"Server Address: http://{local_ip}:5000")
    # app.run(host="0.0.0.0", port=5000, debug=True)
