from flask import Flask;
from flask import render_template;
import pythonbdd;
app= Flask(__name__, template_folder='./view', static_url_path='/view/assets')

@app.route('/')
def index():
	return render_template('index.html');

@app.route('/kappa')
def kappa():
	return ':kappa'

@app.route('/issou')
def issou():
    data = pythonbdd.db()
    
    return render_template('mongo.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
