# import KafkaProducer from Kafka Library
from kafka import KafkaProducer

# Server with Port (Name defined on Docker Compose)
bootstrap_servers = ['kafka:9092']

# Topic name where the message will publish
topicName = 'uberblack'

# Initialize the producer variable
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)

# send message to defined topic
producer.send(topicName, b'Minha Primeira mensagem')

# Print message
print("Mensagem Enviada")