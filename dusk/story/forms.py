#story/forms.py
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class StoryForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    text = TextAreaField('Text',validators=[DataRequired()])
    submit = SubmitField("Post")

