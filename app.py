from flask import Flask, request, jsonify
from client import Client
from ticket import Ticket
import uuid

app = Flask(__name__)

# client methods

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
                        active= data_client["active"])
    
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


@app.route("/client/<int:id>", methods=['GET'])
def get_client(id):
    for client in client_list:
        if client["client_id"] == id:
            return jsonify(client), 200
        
    return jsonify({
        "message": "client not found"
    }), 404


@app.route("/client/<int:id>", methods=['PUT'])
def update_client(id):
    data_client = request.get_json()

    for client in client_list:
        if client["client_id"] == id:
            client["name"] = data_client["name"]
            client["email"] = data_client["email"]
            client["age"] = data_client["age"]
            client["active"] = data_client["active"]

            return jsonify(
                {
                    "message": "client updated",
                    "client": client
                }
            ), 200

    return jsonify({"message": "client not found"}), 404

    
@app.route("/client/<int:id>", methods=['DELETE'])
def delete_client(id):
    for client in client_list:
        if client["client_id"] == id:
            client_list.remove(client)
            print(client_list)
    
    return jsonify (
        {"message": "client deleted"}
        ) , 200

# ticket methods

tickets_list = []

@app.route("/ticket", methods=['POST'])
def create_ticket():
    ticket_data = request.get_json()
    new_ticket = Ticket(ticket_id= str(uuid.uuid4()),
                        client_id= ticket_data["client_id"],
                        title= ticket_data["title"],
                        description= ticket_data["description"],
                        category= ticket_data["category"],
                        urgency= ticket_data["urgency"],
                        priority= ticket_data["priority"],
                        status= ticket_data["status"])

    tickets_list.append(new_ticket.to_dict())

    print(tickets_list)

    return jsonify(
        {"message":"ticket created",
         "created_ticket": ticket_data}
        ), 200

@app.route("/tickets", methods=['GET'])
def get_tickets():
    return jsonify({
        "created_tickets": len(tickets_list),
        "tickets_list": tickets_list
    }), 200


@app.route("/ticket/<ticket_id>", methods=['GET'])
def get_ticket(ticket_id):
    for ticket in tickets_list:
        if ticket["ticket_id"] == ticket_id:
            return jsonify(
                {
                    "message": "ticket found",
                    "ticket": ticket
                }
            ), 200

    return jsonify({"message": "ticket not found"}), 404



if __name__ == "__main__":
    app.run(debug=True)
