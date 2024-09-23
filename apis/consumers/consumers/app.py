from chalice import Chalice

app = Chalice(app_name='consumers')
users = {
            "users": [
                {"name": "usuário1", "phone": "47999999999"},
                {"name": "usuário2", "phone": "47999999999"},
                {"name": "usuário3", "phone": "47999999999"},
            ]
        }


companies = {
                "companies": [
                    {"name": "empresa1", "telefone": "47999999999"},
                    {"name": "empresa2", "telefone": "37999999999"},
                    {"name": "empresa3", "telefone": "27999999999"},
                ]
            }


@app.route('/consumers/person', methods=['POST'])
def create_user():
    # 
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Usuário {requests_params} criado com sucesso!"
    }
    return response

@app.rout('/consumers/person', methods=['PUT'])
def update_user():
    resquest_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Usuário {resquest_params} atualizado com sucesso!"    
    }
    return response

@app.route('/consumers/person', methods=['DELETE'])
def delete_user():
    resquest_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Usuário {resquest_params} deletado com sucesso!"    
    }
    return response

@app.route('/consumers/person', methods=['GET'])
def get_person():
    response = {
        "statusCode": 200,
        "body": users
    }
    return response

