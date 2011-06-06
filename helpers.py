from flask import request, session, redirect
from urllib import urlencode
import datetime
from bson.objectid import ObjectId
from bson.code import Code
from bson.binary import Binary
import hashlib, math, re
from settings import BASE_DIR
from markdown import markdown

function_table = {
	datetime.datetime: lambda obj: obj.strftime("datetime('%Y-%m-%d %H:%M:%S')"),
	ObjectId: lambda obj: 'oid('+repr(str(obj))+')',
	Code: lambda obj: 'code('+repr(str(obj))+')',
	Binary: lambda obj: 'bin('+repr(str(obj))+')',
	re._pattern_type: lambda obj: 'regex('+repr(obj.pattern)+')',
	dict: lambda obj: '{'+', '.join([encode(key)+': '+encode(val) for key,val in obj.items()])+'}',
	list: lambda obj: [encode(sub) for sub in obj]
}

def login_required(route):
	def check_login(**args):
		if session.get('username'):
			return route(**args)
		print(request.path)
		qstr = urlencode({'redirect':request.path})
		return redirect('/login?'+qstr)
	check_login.__doc__ = route.__doc__
	check_login.__name__ = route.__name__
	return check_login
	
def safe_eval(code):
	def sha256(plain):
		return hashlib.sha256(plain).hexdigest()
	def sha1(plain):
		return hashlib.sha1(plain).hexdigest()
	def md5(plain):
		return hashlib.md5(plain).hexdigest()
	def new_date(dstr):
		return datetime.datetime.strptime(dstr, '%Y-%m-%d %H:%M:%S')
	return eval(code, {'oid':ObjectId, 'code':Code, 'bin':Binary,
			'datetime':datetime, 'now':datetime.datetime.now, 'datetime':new_date, 
			'sha256':sha256, 'sha1': sha1, 'md5':md5,
			'regex':re.compile, 'math':math})
			
def encode(obj):
	converter = function_table.get(type(obj))
	if converter:
		return converter(obj)
	return repr(obj)
	
def get_documentation(name):
	f = open(BASE_DIR+'/doc/'+name+'.md')
	return markdown(f.read(), ['codehilite'])
