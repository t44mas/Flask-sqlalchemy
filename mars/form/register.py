from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, EmailField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Login / email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_again = PasswordField('Repeat password', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    speciality = StringField('Position')
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Submit')
