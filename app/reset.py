from app.models import *

db.drop_all()
db.create_all()

u1 = User(name="Jason", email="jason@me.com")
u2 = User(name="Michael", email="michael@me.com")
u3 = User(name="Shafeeq", email="imshafeeq@me.com")
db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
db.session.commit()