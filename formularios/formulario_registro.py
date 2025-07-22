from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DecimalField, DateField, TextAreaField
from wtforms.validators import InputRequired, Length, Email, NumberRange

class FormularioRegistro(FlaskForm):
    nombre_usuario = StringField('Nombre de usuario', validators=[InputRequired(), Length(min=4, max=150)])
    correo = StringField('Correo electrónico', validators=[InputRequired(), Email()])
    contrasena = PasswordField('Contraseña', validators=[InputRequired()])
    enviar = SubmitField('Registrarse')