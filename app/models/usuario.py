from extensiones import db
from flask_login import UserMixin


class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(150), unique=True, nullable=False)
    correo = db.Column(db.String(150), unique=True, nullable=False)
    contrasena = db.Column(db.String(200), nullable=False)

    transacciones = db.relationship('Transaccion', backref='usuario', lazy=True)
    categorias = db.relationship('Categoria', backref='usuario', lazy=True)
