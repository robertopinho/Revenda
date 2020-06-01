from banco import db
from datetime import datetime


class Carro(db.Model):
    __tablename__ = 'carros'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    modelo = db.Column(db.String(40), nullable=False)
    cor = db.Column(db.String(30), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    data_cad = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    imagem = db.Column(db.String(120), nullable=False)
    destaques = db.Column(db.String(1))

    marca_id = db.Column(db.Integer, db.ForeignKey(
        'marcas.id'), nullable=False)

    marca = db.relationship('Marca')

    def to_json(self):
        json_carros = {
            'id': self.id,
            'modelo': self.modelo,
            'cor': self.cor,
            'ano': self.ano,
            'preco': self.preco,
            'marca_id': self.marca_id,
            'marca': self.marca.nome,
            'imagem': self.imagem,
            'destaques': self.destaques

        }
        return json_carros

    @staticmethod
    def from_json(json_carros):
        modelo = json_carros.get('modelo')
        cor = json_carros.get('cor')
        ano = json_carros.get('ano')
        preco = json_carros.get('preco')
        marca_id = json_carros.get('marca_id')
        imagem = json_carros.get('imagem')
        destaques = json_carros.get('destaques')
        return Carro(modelo=modelo, cor=cor, ano=ano, preco=preco, marca_id=marca_id, imagem=imagem, destaques=destaques)

