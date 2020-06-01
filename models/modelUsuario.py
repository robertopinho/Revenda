from banco import db
import hashlib
from config import config

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    senha = db.Column(db.String(32), nullable=False)

    def to_json(self):
        json_usuarios = {
            'id': self.id,
            'nome': self.nome,
            'email': self.email
        }
        return json_usuarios

    @staticmethod
    def from_json(json_usuarios):
        nome = json_usuarios.get('nome')
        email = json_usuarios.get('email')
        senha = json_usuarios.get('senha') + config.SALT
        senha_md5 = hashlib.md5(senha.encode()).hexdigest()        
        return Usuario(nome=nome, email=email, senha=senha_md5)
