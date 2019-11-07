from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField , TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.fields.html5 import TelField
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from TrungtinBlog.models import User


class RegistrationForm(FlaskForm):
    fullname = StringField('Full Name', validators=[DataRequired()])
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=6, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    telephone = TelField('Telephone',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email is taken. Please choose a different one.')
                
    def validate_telephone(self, telephone):
        user = User.query.filter_by(telephone=telephone.data).first()
        if user:
            raise ValidationError('That telephone is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=6, max=12)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    fullname = StringField('Full Name',
                           validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    telephone = TelField('Telephone',
                         validators=[DataRequired()])
    picture = FileField('Update profile picture', validators=[
                        FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_telephone(self, telephone):
        if telephone.data != current_user.telephone:
            user = User.query.filter_by(telephone=telephone.data).first()
            if user:
                raise ValidationError(
                    'That telephone is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    'That email is taken. Please choose a different one.')


class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(
                'There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
