
import firebase_admin
from firebase_admin import credentials, messaging

# Initialize Firebase app with service account key
cred = credentials.Certificate('C:\Users\Shivam Dave\Downloads\ally-vate-firebase-adminsdk-89rmo-f11eb3e012.json')
firebase_admin.initialize_app(cred)

# Send notification
message = messaging.Message(
    notification=messaging.Notification(
        title='Title of the Notification',
        body='Body of the Notification'
    ),
    topic='topic_name'
)

response = messaging.send(message)
print('Successfully sent message:', response)

