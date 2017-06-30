from flask import Flask;
from flask import render_template;

app= Flask(__name__, template_folder='./view')

@app.route('/')
def index():
	return render_template('index.html');

@app.route('/kappa')
def kappa():
	return ':kappa'

@app.route('/issou')
def issou():
	return 'issou'

# if __name__ =='__main__':
# 	app.run(debug=True)