from .models import Player
from werkzeug import exceptions
from flask import jsonify, request
from . import db

def index():
  try:
    players = Player.query.all()
    data = [p.json for p in players]
    return jsonify({"players": data})
  except:
    raise exceptions.InternalServerError("We are working on it")

def create():
  try:
    name, age, position = request.json.values()
    new_player = Player(name, age, position)
    
    db.session.add(new_player)
    db.session.commit()

    return jsonify({"data": new_player.json}), 201
  except:
    raise exceptions.BadRequest(f"We cannot procces your request, age, name, and position are required and you only provided ")

def show(id):
  try:
    player = Player.query.filter_by(id=id).first()
    return jsonify({"data": player.json}), 200
  except:
    raise exceptions.NotFound("")

def update(id):
  data = request.json
  player = Player.query.filter_by(id=id).first()

  for (attribute, value) in data.items():
    if hasattr(player, attribute):
      setattr(player, attribute, value)

    db.session.commit()

    return jsonify({ "data": player.json })

def destroy(id):
  try:
    player = Player.query.filter_by(id=id).first()
    db.session.delete(player)
    db.session.commit()
    return f"Player Deleted"
  except:
    raise exceptions.NotFound("failed to delete")
