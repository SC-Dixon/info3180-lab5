# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class MovieForm(FlaskForm):
    title = StringField('title', validators=[InputRequired()])
    description = TextAreaField('description', validators=[InputRequired()])
    poster = FileField('poster', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images Only!')])
    