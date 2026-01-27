from flask import Flask, request, jsonify
from client import Client

app = Flask(__name__)

client_list = []
client_id = 1

@app.route("/client", methods=['POST'])
def create_client():
    global client_id

    data_client = request.get_json()
    new_client = Client(client_id= client_id,
                        name= data_client["name"],
                        email= data_client["email"],
                        age= data_client["age"],
                        active= True)
    
    client_list.append(new_client.to_dict())
    client_id = client_id + 1

    return jsonify(
        {"message":"Customer successfully registered."},
    ), 200


@app.route("/clients", methods=['GET'])
def get_clients():
    return jsonify(
        {
            "total_clients": len(client_list),
            "clients" : client_list
        }
    ), 200


@app.route("/clients/<int:id>", methods=['GET'])
def get_client(id):
    for client in client_list:
        if client["client_id"] == id:
            return jsonify(client), 200
        
    return jsonify({
        "message": "client not found"
    }), 404


if __name__ == "__main__":
    app.run(debug=True)