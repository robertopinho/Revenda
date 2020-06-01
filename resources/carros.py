from flask import Blueprint, jsonify, request
from banco import db
from models.modelCarro import Carro
from flask_jwt_extended import jwt_required
from flask_cors import CORS, cross_origin

carros = Blueprint('carros', __name__)


@carros.route('/carros')
def listagem():
    carros = Carro.query.order_by(Carro.modelo).all()
    return jsonify([carro.to_json() for carro in carros])


@carros.route('/carros/destaques')
def destaques():
    carros = Carro.query.order_by(Carro.modelo).filter(
        Carro.destaques == 'x').all()
    return jsonify([carro.to_json() for carro in carros])


@carros.route('/carros/destacar/<int:id>',  methods=['PUT'])
def destacar(id):
    #idd = request.json.get('id', None)

    carro = Carro.query.get_or_404(id)

    carros = Carro.query.order_by(Carro.modelo).filter(
        Carro.id == id).one()

    val = carros.destaques

    if (val == ""):
        carro.destaques = "x"

        db.session.add(carro)
        db.session.commit()
        return jsonify({"msg": "Destaque Adicionado!"}), 200
    else:
        carro.destaques = ""

        db.session.add(carro)
        db.session.commit()
        return jsonify({"msg": "Destaque removido!"}), 200


@carros.route('/carros/pesq/<palavra>')
def pesquisa(palavra):
    carros = Carro.query.order_by(Carro.id).filter(
        Carro.modelo.like(f'%{palavra}%')).all()
    if (len(carros) == 0):
        return jsonify({"msg": "Modelo não encontrado"}), 400
    else:
        return jsonify([carro.to_json() for carro in carros])


@carros.route('/carros', methods=['POST'])
#@jwt_required
def inclusao():
    carro = Carro.from_json(request.json)
    db.session.add(carro)
    db.session.commit()
    return jsonify(carro.to_json()), 201
