from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Length, EqualTo, Email
from lista.models import Doctor


class RegisterForm(FlaskForm):
    def validate_email_address(self, email_address_to_check):
        email_address = Doctor.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email address already exists! Try different email address')
    email_address = StringField(validators=[Email(), DataRequired()])
    password = PasswordField(validators=[Length(min=6), DataRequired()])
    password1 = PasswordField(validators=[Length(min=6), DataRequired()])
    submit = SubmitField(label='Create Account')



class LoginForm(FlaskForm):
    email_address = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField(label='Sign in')