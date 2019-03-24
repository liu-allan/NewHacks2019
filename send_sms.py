# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC2c44ad07f782922ea9df3834c284a3f1'
auth_token = '4155d3f93fd88bc384950d39d8a9c70b'
client = Client(account_sid, auth_token)

message = client.messages \
   .create(
        body='Your plant needs watering!',
        from_='+12048139907',
        to='+12042931928'
    )
print(message.sid)