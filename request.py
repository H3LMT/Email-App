from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/main')
def home():
	return render_template('index.html')

@app.route('/about')
def hi():
   return render_template('about.html')

@app.route('/hello',methods =['POST'])
def hello_name():
   print(request.form['name'])
   return render_template('return.html',email=request.form['name'])

if __name__ == '__main__':
   app.run(debug = True)