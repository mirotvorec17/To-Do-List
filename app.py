from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)
    deadline = db.Column(db.Date, nullable=False)
    def __repr__(self):
        return f'<Task {self.content}>'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        deadline = request.form['deadline']
        new_task = Task(content=content, deadline=datetime.strptime(deadline, '%Y-%m-%d').date())

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'не удалось добавить задачу'

    else:
        tasks = Task.query.order_by(Task.deadline).all()
        return render_template('index.html', tasks=tasks)

@app.route('/complete/<int:id>')
def complete_task(id):
    task = Task.query.get_or_404(id)
    try:
        task.done = True
        db.session.commit()
        return redirect('/')
    except:
        return 'возникла проблема с выполнением вашей задачи'

@app.route('/delete/<int:id>')
def delete_task(id):
    task = Task.query.get_or_404(id)
    try:
        db.session.delete(task)
        db.session.commit()
        return redirect('/')
    except:
        return 'не удалось удалить задачу'

if __name__ == "__main__":
    app.run(debug=True)
