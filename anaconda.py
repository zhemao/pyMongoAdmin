#!/usr/bin/python2

from flask import Flask, session, request, render_template, redirect
from database import *
from helpers import *
import hashlib
import settings
import datetime
from bson.objectid import ObjectId

app = Flask(__name__)
app.config.from_object(settings)

@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		url = request.form['redirect']
		if check_user(username, password):
			session['username'] = username
			return redirect(url)
		return render_template('login.html', 
				error='Incorrect username of password', redirect=url)
	url = request.args.get('redirect','/')
	return render_template('login.html', error=None, redirect=url)

@app.route('/')
@app.route('/db')
@login_required
def databases():
	databases = conn.database_names()
	return render_template('databases.html', databases=databases)
	
@app.route('/db/<db>')
@login_required
def collections(db):
	collections = conn[db].collection_names()
	return render_template('collections.html', collections=collections, db=db)
				
@app.route('/db/<db>/coll/<coll>')
@login_required
def documents(db, coll):
	if 'q' in request.args and request.args['q']:
		q = safe_eval(request.args['q'])
	else: q = {}
	documents = conn[db][coll].find(q)
	return render_template('documents.html', documents=documents, 
			db=db, coll=coll, encode=encode, query=q)
			
@app.route('/db/<db>/coll/<coll>/doc/<oid>',methods=['GET','POST'])
@login_required
def edit(db, coll, oid):
	if request.method == 'POST':
		doc = {}
		for key, val in request.form.items():
			doc[key] = safe_eval(val)
		conn[db][coll].save(doc)
		return redirect('/db/'+db+'/coll/'+coll)
	if oid!='new': 
		doc = conn[db][coll].find_one(ObjectId(oid))
	else: doc = {}
	return render_template('edit.html',doc=doc,db=db,coll=coll,oid=oid,encode=encode)
	
@app.route('/db/<db>/coll/<coll>/doc/<oid>/delete')
@login_required
def delete_doc(db, coll, oid):
	conn[db][coll].remove(ObjectId(oid))
	return redirect('/db/'+db+'/coll/'+coll)

@app.route('/db/<db>/coll/<coll>/delete')
@login_required
def delete_coll(db, coll):
	conn[db].drop_collection(coll)
	return redirect('/db/'+db)
	
@app.route('/db/<db>/delete')
@login_required
def delete_db(db):
	conn.drop_database(db)
	return redirect('/')
	
@app.route('/doc/<name>')
def documentation(name):
	body = get_documentation(name)
	return render_template('userdocs.html', body=body)

@app.route('/logout')
def logout():
	del session['username'] 
	return redirect('/login')

if __name__=='__main__':
	app.run()
