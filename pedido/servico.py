from flask import Flask, request
from kafka import KafkaProducer
import json

app = Flask(__name__)

producer = KafkaProducer(
  bootstrap_servers = "kafka:29092",
  value_serializer=lambda v: json.dumps(v)encode("utf-8")
)

@app.route("/pedido", methods=["POST"])
def criar_pedido():
  dados = request.json
  producer.send("pedido_criado", dados)
  return {"mensagem": "Pedido enviado com sucesso"}, 201

if __name__ == "__main__":
  app.run(host:"0.0.0.0", port=5000)
  
  