# formularios.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DecimalField, DateField, TextAreaField
from wtforms.validators import InputRequired, Length, Email, NumberRange


class FormularioTransaccion(FlaskForm):
    monto = DecimalField('Monto', validators=[InputRequired(), NumberRange(min=0.01)])
    tipo = SelectField('Tipo de transacción', choices=[('Ingreso', 'Ingreso'), ('Egreso', 'Egreso')], validators=[InputRequired()])
    categoria = SelectField('Categoría', coerce=int, validators=[InputRequired()])
    fecha = DateField('Fecha', format='%Y-%m-%d', validators=[InputRequired()])
    descripcion = TextAreaField('Descripción (opcional)')
    enviar = SubmitField('Guardar transacción')
