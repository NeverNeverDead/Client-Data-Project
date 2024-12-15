import pika
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:strongpassword@database/insurance_data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    policy = db.Column(db.String(50), nullable=False)

def send_message(queue_name, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('message_queue'))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_publish(exchange='', routing_key=queue_name, body=message)
    print(f" [x] Sent '{message}'")
    connection.close()

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/clients', methods=['GET'])
def get_clients():
    clients = Client.query.all()
    return jsonify([{"id": client.id, "name": client.name, "policy": client.policy} for client in clients])

@app.route('/clients', methods=['POST'])
def create_client():
    data = request.get_json()
    if not data or 'name' not in data or 'policy' not in data:
        return jsonify({"message": "Недостаточно данных!"}), 400
    new_client = Client(name=data['name'], policy=data['policy'])
    db.session.add(new_client)
    db.session.commit()
    send_message('client_creation_queue', f"Клиент создан: {new_client.name}")
    return jsonify({"message": "Клиент создан!", "id": new_client.id}), 201

@app.route('/clients/search', methods=['GET'])
def search_clients():
    query = request.args.get('query')
    if not query:
        return jsonify({"message": "Введите запрос для поиска!"}), 400
    clients = Client.query.filter(Client.name.ilike(f"%{query}%")).all()
    return jsonify([{"id": client.id, "name": client.name, "policy": client.policy} for client in clients])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
