from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DecimalField, DateField, TextAreaField
from wtforms.validators import InputRequired, Length, Email, NumberRange


class FormularioCategoria(FlaskForm):
    nombre = StringField('Nombre de la categoría', validators=[InputRequired(), Length(max=100)])
    enviar = SubmitField('Guardar categoría')