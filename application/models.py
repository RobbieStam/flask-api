from application import db, app

app.app_context().push()

class Player(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  age = db.Column(db.Integer, nullable=False)
  position = db.Column(db.String(2), nullable=False)

  def __init__(self, name, age, position):
    self.name = name
    self.age = age
    self.position = position
    

  def __repr__(self):
    return f"Player(id: {self.id}, name: {self.name}, position: {self.position})"

  @property
  def json(self):
    return {"id": self.id, "name": self.name, "age": self.age, "position": self.position}
