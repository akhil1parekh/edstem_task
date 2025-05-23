from kafka import KafkaConsumer
import json

consumer = KafkaConsumer("user_activity",value_deserializer = lambda m: json.loads(m.decode("utf-8")))

for message in consumer:
    print(f"Recieved {message.value}")