from flask import Flask, jsonify, request
from flask import Blueprint 
from config import config
from banco import db
from resources.carros import carros
from resources.marcas import marcas
from resources.propostas import propostas
from resources.usuarios import usuarios
from flask_jwt_extended import JWTManager
from blacklist import blacklist
from flask_cors import CORS
import smtplib
from models.modelProposta import Proposta


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
jwt = JWTManager(app)

# libera todas as ROTAS (não é a melhor forma, em termo de segurança)
# melhor forma é a do exemplo anterior, indicar quais rotas devem ser liberadas para o acesso CORS
CORS(app)

app.register_blueprint(carros)
app.register_blueprint(marcas)
app.register_blueprint(usuarios)
app.register_blueprint(propostas)


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist


@app.route('/')
def raiz():
    return '<h2>Revenda Herbie</h2>'

@app.route('/envia_email')
def envia():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('robertopinhocardozo@gmail.com', 'As84374555')
    server.set_debuglevel(1)
    server.sendmail('robertopinhocardozo@gmail.com',
                    'robertoopinho@gmail.com',
                    'Subject: Revenda Herbie - Proposta\nRecebemos sua proposta, logo entraremos em contato.\n Proposta:  ')
    server.quit()
    return jsonify({"Message": "E-mail enviado..."})


@app.route('/criadb')
def criadb():
    db.create_all()
    return "Ok! Tabelas criadas com sucesso"


if __name__ == '__main__':
    app.run(debug=True)
