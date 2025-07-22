from extensiones import db
from flask_login import UserMixin

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    transacciones = db.relationship('Transaccion', backref='categoria', lazy=True)
