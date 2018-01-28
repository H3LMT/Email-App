# Email App
Simple email web app to send emails with

##Required Modules
- Python 3.0+
- Python Flask Module (pip install flask)
- Python NumPy Module (pip install numpy)
- Python Requests Module (pip install requests)

## Setup API's
This web app requires two services. 
[Mailgun](https://www.mailgun.com/) and [Sendgrid](https://sendgrid.com/)
It's easy to make accounts for both of these services. In order to use mailgun you will need to collect both your unique API key as well as your sandbox link. In order to use SendGrid, just the API key is necessary. In the request.py file, there are three variables that need to be updated. 
- `mailgunSandbox` - mailgun sandbox link
- `mailgunKey` - mailgun API key
- `sendgrid` - sendgrid API key 

##Running The App
- Change directory to where requests.py is located
- In the shell run python requests.py and a local server will be created
- Navigate to http://127.0.0.1:5000/main

##Testing
All fields are required from the user and the form cannot be submitted until all fields have an input. The webapp first tries to use the mailgun service and if it fails (i.e. email that is not registered in mailgun service), it will automatically without user input switch to the sendgrid service which is much more lenient. Once submitted a new tab will open showing the address the email was sent to as well as which provider was used. If both services fail, a message will be displayed showing that the e-mail was not delivered. 

To test whether it autmoatically switches over to sendgrid, a bad api key can be used, or a email that is not registered in the mailgun service is used. 

