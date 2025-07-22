from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DecimalField, DateField, TextAreaField
from wtforms.validators import InputRequired, Length, Email, NumberRange
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DecimalField, DateField, TextAreaField
from wtforms.validators import InputRequired, Length, Email, NumberRange

class FormularioInicioSesion(FlaskForm):
    correo = StringField('Correo electrónico', validators=[InputRequired(), Email()])
    contrasena = PasswordField('Contraseña', validators=[InputRequired()])
    enviar = SubmitField('Iniciar sesión')