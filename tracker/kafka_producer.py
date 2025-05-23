from kafka import KafkaProducer
import json

producer = KafkaProducer(
   
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

def send_activity_event(event_data):
    producer.send("user_activity",event_data)
    producer.flush()