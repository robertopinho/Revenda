from flask import Blueprint, jsonify, request
from banco import db
from models.modelProposta import Proposta
from flask_jwt_extended import jwt_required
from flask_cors import CORS, cross_origin
from models.modelCarro import Carro
from models.modelMarca import Marca
import json
import smtplib


propostas = Blueprint('propostas', __name__)


@propostas.route('/propostas')
def listagem():
    propostas = Proposta.query.order_by(Proposta.id).all()
    return jsonify([proposta.to_json() for proposta in propostas])


@propostas.route('/propostas/status')
def status():
    carros = Carro.query.order_by(Carro.modelo).all()
    propostas = Proposta.query.order_by(Proposta.id).all()
    marcas = Marca.query.order_by(Marca.id).all()
    totalCarros = 0
    totalPropostas = 0
    totalMarcas = 0
    totalCarros += len(carros)
    totalPropostas += len(propostas)
    totalMarcas += len(marcas)
    totalPreco = 0
    t = 0
    for i in enumerate(carros):
        totalPreco += carros[t].preco
        t += 1
    return jsonify({"Estatisticas": f'Total de carros cadastrados: {totalCarros}  Total de propostas: {totalPropostas} Total de marcas: {totalMarcas} Total de valor em carros: {totalPreco}'})


@propostas.route('/propostas/pesq/<palavra>')
def pesquisa(palavra):
    propostas = Proposta.query.order_by(Proposta.id).filter(
        Proposta.carro_id.like(f'%{palavra}%')).all()
    if (len(propostas) == 0):
        return jsonify({"msg": "Modelo não encontrado"}), 400
    else:
        return jsonify([proposta.to_json() for proposta in propostas])


@propostas.route('/propostas/<int:id>', methods=['DELETE'])
def exclui(id):
    Proposta.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({'id': id, 'message': 'Proposta excluída com sucesso'}), 200


@propostas.route('/propostas', methods=['POST'])
@jwt_required
def inclusao():
    proposta = Proposta.from_json(request.json)
    email = request.json.get('email', None)
    valor = request.json.get('valor', None)
    carro_id = request.json.get('carro_id', None)
    db.session.add(proposta)
    db.session.commit()
    carros = Carro.query.order_by(Carro.modelo).filter(
        Carro.id == carro_id).one()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('robertopinhocardozo@gmail.com', 'As84374555')
    server.set_debuglevel(1)
    server.sendmail('robertopinhocardozo@gmail.com',
                    [email, 'robertopinhocardozo@gmail.com'],
                    f'Subject: Revenda Herbie - Proposta\nRecebemos sua proposta, logo entraremos em contato.\nProposta ID:{proposta.id} \nCarro ID: {carro_id}\nModelo: {carros.modelo} \n Preco: {valor} ')
    server.quit()

    return jsonify({"Message": "E-mail enviado..."})
