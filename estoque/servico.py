from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
  'pedido_criado',
  bootstrap_servers='kafka:29092',
  group_id='estoque-group',
  value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)