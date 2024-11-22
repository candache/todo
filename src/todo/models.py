from datetime import datetime
from src import db

class ToDoList(db.Model):
    __tablename__ = "todo_lists"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    items = db.relationship('ToDoItem', backref='list', lazy=True)

    def __repr__(self):
        return f"<ToDoList {self.name}>"

class ToDoItem(db.Model):
    __tablename__ = "todo_items"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), nullable=False, default="pending")
    completed = db.Column(db.Boolean, nullable=False, default=False)
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey('todo_lists.id'), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('todo_items.id'), nullable=True)
    children = db.relationship('ToDoItem', backref=db.backref('parent', remote_side=[id]), lazy=True)

    def __repr__(self):
        return f"<ToDoItem {self.title}>"