from app import app
from flask import render_template, request, redirect, url_for
from app.models import *
import pdb

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
	user = {'name': 'Jason Brooks'}
	friends = [{'name': 'Shafeeq Ibraheem'}, {'name': 'Peter Salovey'}]
	return render_template('index.html', title="Homepage", user=user, friends=friends, posts=reversed(Post.query.all()))

@app.route('/new-post', methods=['GET', 'POST'])
def newPost():
	if request.method == 'GET':
		return render_template('new-post.html', title="New Post")
	title = request.form['post-title']
	content = request.form['post-content']
	author_email = request.form['post-author']
	author = User.query.filter(User.email == author_email).first()
	post = Post(title=title, body=content, author=author)
	db.session.add(post)
	db.session.commit()
	post = {'title': title, 'content': content}
	return redirect(url_for('index'))