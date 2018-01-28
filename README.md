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
- 'mailgunSandbox' - mailgun sandbox link
- 'mailgunKey' - mailgun API key
- 'sendgrid' - sendgrid API key 

