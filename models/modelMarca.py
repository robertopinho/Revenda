from banco import db

class Marca(db.Model):
    __tablename__ = 'marcas'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(30), nullable=False)

    carros = db.relationship('Carro')

    def to_json(self):
        json_marcas = {
            'id': self.id,
            'nome': self.nome,
            # 'carros': [carro.to_json() for carro in self.carros]
            'num_carros': len(self.carros)
        }
        return json_marcas

    @staticmethod
    def from_json(json_marcas):
        nome = json_marcas.get('nome')
        return Marca(nome=nome)
