import os
import pika
import sys


def main():
    # Create a connection
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

    #  Create a channel
    channel = connection.channel()

    # Create a queue if it does not exist already and associate it with the channel
    channel.queue_declare(queue="hello")

    def callback(ch, method, properties, body):
        print("[x] received %r" %body)

    # Associate a callback function with the message queue
    channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)

    # Start consuming the messages
    print("[x] waiting for the messages, to exit press Ctrl-C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
