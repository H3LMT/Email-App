from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route('/main')
def home():
	return render_template('index.html')

@app.route('/about')
def hi():
   return render_template('about.html')

@app.route('/submit',methods =['POST'])
def mailGun():
	key = 'key-180607584fe0eed06fdcdc3943e3e6eb'
	sandbox = 'sandbox6521ec12d7024cdab31d45c8b8f47386.mailgun.org'
	name = request.form['name']
	recepient = request.form['email']
	message = request.form['msg']
	request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
	pull = requests.post(request_url, auth=('api', key), data={
	'from':  name+' <excited@samples.mailgun.org>',
	'to': recepient,
	'subject': 'Test',
	'text': message})
	print 'Status: {0}'.format(pull.status_code)
	print 'Body:   {0}'.format(pull.text)
	return render_template('return.html',email=name)

if __name__ == '__main__':
   app.run(debug = True)