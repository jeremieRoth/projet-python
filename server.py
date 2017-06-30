from flask import Flask;
from flask import render_template;
import json;
import logging
from logging.handlers import RotatingFileHandler
app = Flask(__name__, template_folder='./view')

@app.route('/')
def index():
    return render_template('index.html');

@app.route('/kappa')
def kappa():
    return ':kappa:'

@app.route('/issou')
def issou():
    return 'issou'


@app.route('/json')
def jsonParse():
	

	json_data=open("json").read()
	data=json.loads(json_data)
	
	chaine="<html><head></head><body>"
	# if(is_array(data))
	for key in data:
		chaine+="<p>"+str(key)+" : </p>"
		if isinstance(data[key], str):
			chaine+="<p>------"+data[key]+"</p>"
		# else:
		# 	for key2 in data[key]:
		# 		chaine+="<p>------"+str(key2)+" : </p>"
		# 		if isinstance(data[key][key2], list):
		# 			chaine+="<p>------------is dict</p>"
		# 		elif isinstance(data[key][key2], str):
		# 			chaine+="<p>------------"+data[key][key2]+"</p>"



	chaine+="</body></html>"

	return chaine;
	


if __name__ =='__main__':
    app.run(host='0.0.0.0', port='80',debug=True)
