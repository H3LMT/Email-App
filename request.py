from flask import Flask, render_template, request
import requests
import sendgrid
import numpy
from sendgrid.helpers.mail import *

app = Flask(__name__)

mailgunSandbox = "YOUR_SANDBOX_HERE"
mailgunKey = "YOUR_KEY_HERE"
sendgridKey= "YOUR_KEY_HERE"

@app.route('/main')
def home():
	return render_template('index.html')

@app.route('/about')
def hi():
   return render_template('about.html')

@app.route('/submit',methods =['POST'])
def sendMail():
	global mailgunKey
	global mailgunSandbox
	global sendgridKey
	if(mailgunSandbox=="YOUR_SANDBOX_HERE" or mailgunKey =="YOUR_KEY_HERE" or sendgridKey=="YOUR_KEY_HERE"):
		mailgunKey = str(numpy.load("./keys/mgkey.npy"))
		mailgunKey = "1234"
		sendgridKey = str(numpy.load("./keys/sg.npy"))
		mailgunSandbox = str(numpy.load("./keys/mgsbx.npy"))

	#form data
	name = request.form['name']
	sender = request.form['from']
	recepient = request.form['to']
	subject = request.form['subject']
	message = request.form['msg']

	#mail gun info
	key = mailgunKey
	sandbox = mailgunSandbox

	#try mailgun
	provider = "Mailgun"
	request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
	pull = requests.post(request_url, auth=('api', key), data={
	'from':  name+'<'+sender+'>',
	'to': recepient,
	'subject': subject,
	'text': message})
	condition = True
	print 'Status: {0}'.format(pull.status_code)
	print 'Body:   {0}'.format(pull.text)

	if(pull.status_code!=200): #if mailgun fails try sendgrid
		provider = "SendGrid"
		sg = sendgrid.SendGridAPIClient(apikey=sendgridKey)
		from_email = Email("test@example.com")
		to_email = Email(recepient)
		subject = "Sending with SendGrid is Fun"
		content = Content("text/plain", message)
		mail = Mail(from_email, subject, to_email, content)
		response = ""
		try:
			response = sg.client.mail.send.post(request_body=mail.get())
			print("WDJOJWD W")
			print(response.status_code)
			print(response.body)
			print(response.headers)
		except:
			print("FWJOJOE L")
			condition = False		

	#status message
	status = "Your message to <"+recepient+"> was delivered by "+provider+"."
	if(condition==False):
		status = "Your message to <"+recepient+"> failed to deilver"
	return render_template('return.html',message=status)

if __name__ == '__main__':
   app.run(debug = True)