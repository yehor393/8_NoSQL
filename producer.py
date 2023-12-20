import pika
from faker import Faker
from mongoengine import connect, Document, StringField, BooleanField
import json

fake = Faker()

# Підключення до MongoDB
connect('email_contacts', host='mongodb://localhost:27017/email_contacts')


class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    message_sent = BooleanField(default=False)


# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='email_queue')

# Генерація фейкових контактів та надсилання їх до черги RabbitMQ
for _ in range(5):  # Змініть кількість контактів за необхідності
    contact_data = {
        'full_name': fake.name(),
        'email': fake.email(),
    }

    contact = Contact(**contact_data).save()
    message = {'contact_id': str(contact.id)}
    channel.basic_publish(exchange='', routing_key='email_queue', body=json.dumps(message))

    print(f"Contact {contact.full_name} added to the queue.")

connection.close()
