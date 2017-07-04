from flask import Flask , request;
from flask import render_template;
from flask import redirect, url_for;
import xml.etree.ElementTree as ET
import json;
import logging;
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





@app.route('/recuptext', methods=['GET', 'POST'])
def recupTxt():
	if request.method == 'POST':
		# return "{file}".format(file=request.form['file'])
		return redirect(url_for('text',url=request.form['txt']))
	return render_template('recup.html');

@app.route('/text/<url>')
def text(url):
	return url



@app.route('/recupFile', methods=['GET', 'POST'])
def recupFile():
	if request.method == 'POST':
		file = request.files['file']

		global json_file 
		json_file= '/tmp/'+file.filename

		file.save(json_file)
		if file.filename.endswith((".json")):
			return redirect(url_for('jsonParse'))
		# return "{file}".format(file=request.form['file'])
		# return redirect(url_for('jsonParse',file2=request.file['file']))
	return render_template('recupFile.html');


@app.route('/json')
def jsonParse():

	return json_file

	# json_data=open(file2).read()
	# data=json.loads(json_data)
	# return data["menu"]
	# chaine="<html><head></head><body>"

	# if(is_array(data))
	# for key in data:
	# 	chaine+="<p>"+str(key)+" : </p>"
	# 	if isinstance(data[key], str):
	# 		chaine+="<p>------"+data[key]+"</p>"
	# 	else:
	# 		for key2 in data[key]:
	# 			chaine+="<p>------"+str(key2)+" : </p>"
	# 			if isinstance(data[key][key2], list):
	# 				chaine+="<p>------------is dict</p>"
	# 			elif isinstance(data[key][key2], str):
	# 				chaine+="<p>------------"+data[key][key2]+"</p>"



	# chaine+="</body></html>"

	# return chaine;
	


if __name__ =='__main__':
    app.run(host='0.0.0.0', port='80',debug=True)
