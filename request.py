from flask import Flask, render_template
app = Flask(__name__)

@app.route('/main')
def wwwww():
	return render_template('index.html')

@app.route('/hello',methods =['POST'])
def hello_name():
   return render_template('about.html')

if __name__ == '__main__':
   app.run(debug = True)