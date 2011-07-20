import hashlib
from pymongo import Connection
import settings

conn = Connection(settings.HOST, settings.PORT)

def get_user(username):
	db = conn.pymongoadmin
	return db.users.find_one({'username':username})
	
def create_user(username, password):
	db = conn.pymongoadmin
	password = hashlib.sha256(password).hexdigest()
	db.users.insert({'username':username, 'password':password})
	
def change_password(username, password):
	db = conn.pymongoadmin
	password = hashlib.sha256(password).hexdigest()
	db.users.find_and_modify({'username':username}, {'password':password},True)
	
def check_user(username, password):
	password = hashlib.sha256(password).hexdigest()
	user = get_user(username)
	return user != None and user['password'] == password


