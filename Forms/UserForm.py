from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, PasswordField
from wtforms import validators


class UserForm(FlaskForm):
    user_name = StringField("Name: ", [
        validators.DataRequired("Please enter your name."),
        validators.Length(2, 20, "Name should be from 2 to 20 symbols")
    ])
    username = StringField("Login: ", [
        validators.DataRequired("Please enter your login."),
        validators.Length(2, 255, "Login should be from 2 to 255 symbols")
    ])
    password = PasswordField("Password: ", [
        validators.DataRequired("Please enter your password."),
        validators.Length(8, 255, "Password should be from 8 to 255 symbols")
    ])
    user_email = StringField("Email: ", [
        validators.DataRequired("Please enter your email."),
        validators.Email("Wrong email format")
    ])
    user_birthday = DateField("Birthday: ", [validators.DataRequired("Please enter your birthday.")])
    user_phone = StringField("Phone: ", [validators.DataRequired("Please enter your phone."),
                                         validators.Length(20)])

    submit = SubmitField("Save")