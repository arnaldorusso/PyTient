from pytient_app import db
import datetime

class Register_patient(db.Model):
    """Register fields"""
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime(datetime.datetime.now()))
    nome = db.Column(db.String(40))
    rg = db.Column(db.String(12))
    nascimento = db.Column(db.String(12))
    # endereco = db.Column(db.String(63))
    # numero = db.Column(db.String(12))
    # complemento = db.Column(db.String(25))
    # bairro = db.Column(db.String(25))
    # convenio = db.Column(db.String(25))
    # exame = db.Column(db.String(25))
    # valor = db.Column(db.String(12))

    # def __init__(self, nome, rg):
    #     self.nome = nome
    #     self.rg = rg
