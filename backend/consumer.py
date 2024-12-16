import pika

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")

def consume_messages(queue_name):
    connection = pika.BlockingConnection(pika.ConnectionParameters('message_queue'))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

consume_messages('client_creation_queue') 
