from flask import Flask
from flask import render_template
import pythonbdd

app = Flask(__name__, template_folder='./view', static_url_path='/view/assets')

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

if __name__ == '__main__':
    app.run(debug=True)
