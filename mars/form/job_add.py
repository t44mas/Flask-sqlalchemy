from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField, BooleanField
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField
from wtforms.validators import DataRequired
from wtforms.fields.numeric import IntegerField


class WorkForm(FlaskForm):
    team_leader = IntegerField('Team Leader id', validators=[DataRequired()])
    job = StringField('Job Title', validators=[DataRequired()])
    work_size = IntegerField('Work Size', validators=[DataRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    is_finished = BooleanField('Is job finished?')
    submit = SubmitField('Submit')
