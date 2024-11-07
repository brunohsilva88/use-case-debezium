from kafka import KafkaConsumer
import json

topicName = 'source.public.payment_streaming'
bootstrap_servers = ['kafka:9092']

consumer = KafkaConsumer(
    topicName,
    auto_offset_reset='earliest',
    bootstrap_servers=bootstrap_servers,
    group_id='payment_id'
)

# Lê e imprime mensagens do consumidor
for msg in consumer:
    try:
        print(json.loads(msg.value))
    except json.JSONDecodeError:
        print("Erro ao decodificar a mensagem JSON:", msg.value)
