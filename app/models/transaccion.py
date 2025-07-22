from extensiones import db
from flask_login import UserMixin


class Transaccion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    monto = db.Column(db.Float, nullable=False)
    tipo = db.Column(db.String(10), nullable=False)  # "Ingreso" o "Egreso"
    fecha = db.Column(db.DateTime, nullable=False)
    descripcion = db.Column(db.String(255))

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
