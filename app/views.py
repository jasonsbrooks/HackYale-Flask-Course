from app import app
from flask import render_template, request
import pdb

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
	user = {'name': 'Jason Brooks'}
	friends = [{'name': 'Shafeeq Ibraheem'}, {'name': 'Peter Salovey'}]
	return render_template('index.html', title="Homepage", user=user, friends=friends)

@app.route('/new-post', methods=['GET', 'POST'])
def newPost():
	if request.method == 'GET':
		return render_template('new-post.html', title="New Post")
	title = request.form['post-title'].lower()
	content = request.form['post-content']
	post = {'title': title, 'content': content}
	return render_template('post.html', post=post)