
from flask import Flask , request, redirect, url_for;
from flask import render_template
import pythonbdd

app = Flask(__name__, template_folder='./view', static_url_path='/view/assets')
import json;

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/classe/<name>')
def classes(name):
    data = pythonbdd.getClass(name)
    return render_template('mongo.html',data=data) 

@app.route('/sClasses')
def sClasses():
    #data = pythonbdd.getSClass(id)
    return render_template('mongo.html')

@app.route('/all')
def all():
    data = pythonbdd.getAll()
    return render_template('mongo.html',data=data) #render_template('mongo.html', data=data)




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
	return render_template('recupFile.html')


@app.route('/json')
def jsonParse():
    json_data=open(json_file).read()
    return json_data
	
if __name__ == '__main__':
    app.run(debug=True)
