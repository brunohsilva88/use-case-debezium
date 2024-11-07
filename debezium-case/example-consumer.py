# import KafkaConsumer from Kafka Library
from kafka import KafkaConsumer

# Server with Port (Name defined on Docker Compose
bootstrap_servers = ['kafka:9092']

# Topic name from where the message will receive
topicName = 'uberblack'

# Initialize the consumer variable
consumer = KafkaConsumer(topicName, auto_offset_reset='earliest', bootstrap_servers = bootstrap_servers)

# read and print the message receveid from consumer
for msg in consumer:
    print("Topic Name:%s, Message:%s"%(msg.topic,msg.value))