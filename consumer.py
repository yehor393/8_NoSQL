import pika
from mongoengine import connect
import json

# Підключення до MongoDB
connect('email_contacts', host='mongodb://localhost:27017/email_contacts')

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='email_queue')


def send_email_stub(contact_id):
    # Функція-заглушка для імітації відправки email
    print(f"Email sent to contact with ID {contact_id}")


# Обробка повідомлень з черги RabbitMQ
def callback(ch, method, body):
    message = json.loads(body)
    contact_id = message.get('contact_id')

    if contact_id is not None:
        send_email_stub(contact_id)

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue='email_queue', on_message_callback=callback)

print("Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
