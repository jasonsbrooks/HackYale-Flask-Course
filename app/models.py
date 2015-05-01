from app import db

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(1000))
	email = db.Column(db.String(1000), unique=True)
	password = db.Column(db.String(1000))

	def __repr__(self):
		return '#%d: Name: %s, Email: %s' %(self.id, self.name, self.email)

class Post(db.Model):
	__tablename__ = 'posts'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(1000))
	body = db.Column(db.String(10000))
	author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	author = db.relationship('User', backref='posts')

	def __repr__(self):
		return '#%d: Title: %s, Body: %s, Author: %s' %(self.id, self.title, self.body, self.author)