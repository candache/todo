from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user

from src import db
from src.todo.models import ToDoList, ToDoItem
from src.todo.forms import ToDoListForm, ToDoItemForm

todo_bp = Blueprint('todo', __name__, template_folder='templates')


@todo_bp.route('/lists')
@login_required
def list_todos():
    lists = ToDoList.query.filter_by(user_id=current_user.id).all()
    return render_template('list.html', lists=lists)

@todo_bp.route('/lists/add', methods=['GET', 'POST'])
@login_required
def add_list():
    form = ToDoListForm()
    if form.validate_on_submit():
        todo_list = ToDoList(name=form.name.data, user_id=current_user.id)
        db.session.add(todo_list)
        db.session.commit()
        flash('ToDo list added successfully!', 'success')
        return redirect(url_for('todo.list_todos'))
    return render_template('add_list.html', form=form)

@todo_bp.route('/lists/<int:list_id>/items/add', methods=['GET', 'POST'])
@login_required
def add_item(list_id):
    form = ToDoItemForm()
    if form.validate_on_submit():
        todo_item = ToDoItem(
            title=form.title.data,
            description=form.description.data,
            status=form.status.data,
            user_id=current_user.id,
            list_id=list_id,
            parent_id=form.parent_id.data or None
        )
        db.session.add(todo_item)
        db.session.commit()
        flash('ToDo item added successfully!', 'success')
        return redirect(url_for('todo.view_list', list_id=list_id))
    return render_template('add_item.html', form=form, list_id=list_id)

@todo_bp.route('/lists/<int:list_id>')
@login_required
def view_list(list_id):
    todo_list = ToDoList.query.get_or_404(list_id)
    if todo_list.user_id != current_user.id:
        flash('You do not have permission to view this list.', 'danger')
        return redirect(url_for('todo.list_todos'))
    items = ToDoItem.query.filter_by(list_id=list_id, parent_id=None).all()
    return render_template('view_list.html', todo_list=todo_list, items=items)

@todo_bp.route('/items/<int:item_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_item(item_id):
    todo_item = ToDoItem.query.get_or_404(item_id)
    if todo_item.user_id != current_user.id:
        flash('You do not have permission to edit this item.', 'danger')
        return redirect(url_for('todo.list_todos'))
    form = ToDoItemForm(obj=todo_item)
    if form.validate_on_submit():
        todo_item.title = form.title.data
        todo_item.description = form.description.data
        todo_item.status = form.status.data
        db.session.commit()
        flash('ToDo item updated successfully!', 'success')
        return redirect(url_for('todo.view_list', list_id=todo_item.list_id))
    return render_template('edit_item.html', form=form)

@todo_bp.route('/items/<int:item_id>/delete', methods=['POST'])
@login_required
def delete_item(item_id):
    todo_item = ToDoItem.query.get_or_404(item_id)
    if todo_item.user_id != current_user.id:
        flash('You do not have permission to delete this item.', 'danger')
        return redirect(url_for('todo.list_todos'))
    db.session.delete(todo_item)
    db.session.commit()
    flash('ToDo item deleted successfully!', 'success')
    return redirect(url_for('todo.view_list', list_id=todo_item.list_id))