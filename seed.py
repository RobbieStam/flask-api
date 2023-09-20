from application import db
from application.models import Player


db.drop_all()
print("Dropping database")
db.create_all()
print("Creating database")

print("Seeding database")

entry1 = Player(name="Lionel Messi", age=36, position="CF")

entry2 = Player(name="Cristiano Ronaldo", age=38, position="LW")

entry3 = Player(name="Marcus Rashford", age=25, position="ST")

db.session.add_all([entry1, entry2, entry3])
db.session.commit()
