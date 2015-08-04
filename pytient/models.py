from pytient_app import db
import datetime

class Register_patient(db.Model):
    """Register fields"""
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40))
    rg = db.Column(db.String(12))
    nascimento = db.Column(db.String(12))
    timestamp = db.Column(db.DateTime, nullable=False)  # (datetime.datetime.now()), nullable=False)
    # endereco = db.Column(db.String(63))
    # numero = db.Column(db.String(12))
    # complemento = db.Column(db.String(25))
    # bairro = db.Column(db.String(25))
    # convenio = db.Column(db.String(25))
    # exame = db.Column(db.String(25))
    # valor = db.Column(db.String(12))

    def __init__(self, nome, rg, nascimento, timestamp):
        # if timestamp is None:
        #     timestamp = datetime.datetime.now()
        self.nome = nome
        self.rg = rg
        self.nascimento = nascimento
        self.timestamp = timestamp
