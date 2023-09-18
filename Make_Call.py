from importlib.resources import path
import os
from twilio.rest import Client
account_sid = 'AC0166af425f2e3fa6e02c771c5871d81e'
auth_token = '783d9d2263b6310121c4057e0f218970'
client = Client(account_sid, auth_token)

#for i in range(5):
#     call = client.calls.create(
#     to= '+919665911930',
#     from_='+13853865788',
#     url='https://file.io/zcJo3HxNHSRD',
#     time_limit = '300'
#     )
#     print(call.sid)

for i in range(10):
    message = client.messages \
                    .create(
                        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                        from_='+13853865788',
                        to='+919665911930'
                    )
    print(message.sid)
