from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, HiddenField
from wtforms.validators import DataRequired

class ToDoListForm(FlaskForm):
    name = StringField('List Name', validators=[DataRequired()])

class ToDoItemForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    status = SelectField('Status', choices=[('pending', 'Pending'), ('completed', 'Completed')])
    parent_id = HiddenField('Parent ID')