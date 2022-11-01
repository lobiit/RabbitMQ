import pika

# Create a connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# Create a channel
channel = connection.channel()

# Create a channel through the channel
channel.queue_declare(queue="hello")

# Publish the message
channel.basic_publish(exchange="", routing_key="hello", body="hello_world msg # 1")
print("[x] Sent Hello World")

# Close the connection
# Automatically closes the channel
connection.close()
