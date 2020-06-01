from banco import db
from datetime import datetime


class Proposta(db.Model):
    __tablename__ = 'propostas'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.String(120))
    email = db.Column(db.String(80), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    data_cad = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    carro_id = db.Column(db.Integer, db.ForeignKey(
        'carros.id'), nullable=False)

    carros = db.relationship('Carro')

    def to_json(self):
        json_propostas = {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'desc': self.desc,
            'valor': self.valor,
            'carro_id': self.carro_id

        }
        return json_propostas

    @staticmethod
    def from_json(json_propostas):
        
        nome = json_propostas.get('nome')
        email = json_propostas.get('email')
        desc = json_propostas.get('desc')
        valor = json_propostas.get('valor')
        carro_id = json_propostas.get('carro_id')
        return Proposta(nome=nome, email=email, desc=desc, valor=valor, carro_id=carro_id)
