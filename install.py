#!/usr/bin/env python2

from pymongo import Connection
import flask, os
from getpass import getpass
import hashlib

if __name__ == '__main__':
	host = raw_input('Host [default localhost]: ') or 'localhost'
	port = int(raw_input('Port [default 27017]: ') or '27017') 
	secret_key = os.urandom(24)
	base_dir = os.getcwd()
	print('writing settings to file...')
	with open('settings.py', 'w') as f:
		f.write('HOST='+repr(host)+'\n')
		f.write('PORT='+str(port)+'\n')
		f.write('SECRET_KEY='+repr(secret_key)+'\n')
		f.write('BASE_DIR='+repr(base_dir)+'\n')
	conn = Connection(host, port)
	user = conn.mongoose.users.find_one()
	if not user:
		print('You do not yet have a user in the database. Would you like to add one now? [y/n]')
		if raw_input() == 'y':
			username = raw_input('Username: ')
			password = getpass()
			confirm = getpass('Confirm Password: ')
			while password!=confirm:
				print('Those passwords don\'t match, please try again.')
				password = raw_input('Password: ')
				confirm = raw_input('Confirm Password: ')
			db = conn.mongoose
			password = hashlib.sha256(password).hexdigest()
			db.users.insert({'username':username, 'password':password})
	print('Finished installation')
