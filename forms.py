from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField


class TodoForm(FlaskForm):
  task = StringField('task')
  discription = TextAreaField('discription')
  done = BooleanField('done', default=False)

  