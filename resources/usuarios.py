from flask import Blueprint, jsonify, request
from banco import db
from models.modelUsuario import Usuario
from config import config
import hashlib
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from blacklist import blacklist

usuarios = Blueprint('usuarios', __name__)


@usuarios.route('/usuarios')
def listagem():
    usuarios = Usuario.query.order_by(Usuario.nome).all()
    return jsonify([usuario.to_json() for usuario in usuarios])


@usuarios.route('/usuarios', methods=['POST'])
def inclusao():
    usuario = Usuario.from_json(request.json)
    db.session.add(usuario)
    db.session.commit()
    return jsonify(usuario.to_json()), 201


@usuarios.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    email = request.json.get('email', None)
    senha = request.json.get('senha', None)
    if not email:
        return jsonify({"msg": "Missing email parameter"}), 400
    if not senha:
        return jsonify({"msg": "Missing senha parameter"}), 400

    senha += config.SALT
    senha_md5 = hashlib.md5(senha.encode()).hexdigest()

    usuario = Usuario.query \
    .filter(Usuario.email == email) \
    .filter(Usuario.senha == senha_md5) \
    .first()

   if usuario:
        access_token = create_access_token(identity=email)
        return jsonify({"user": usuario.nome, "access_token": access_token}), 200
    else:
        return jsonify({"user": None, "access_token": None}), 200
    

@usuarios.route('/logout')
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return jsonify({"msg": "Successfully logged out"}), 200    
