from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField, PasswordField
from wtforms import validators, ValidationError

class RegistrationForm(Form):
   username = TextField("Name Of Student", [validators.Required("Please enter your username.")])
   
   password = PasswordField("password", [validators.Required("Please enter your password.")])
   
   email = TextField("Email",[validators.Required("Please enter your email address."),
    validators.Email("Please enter your email address.")])

   repassword = PasswordField("password",[validators.Required("Please re-enter your password.")])   
   
   submit = SubmitField("Register")

class Login(Form):
   username = TextField("Name Of Student",[validators.Required("Please enter your username.")])
   
   password = PasswordField("password",[validators.Required("Please enter your password.")])


                                                              
