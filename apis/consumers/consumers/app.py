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
                    {"name": "empresa2", "telefone": "47999999999"},
                    {"name": "empresa3", "telefone": "47999999999"},
                ]
            }


@app.route('/')
def index():
    return {'hello': 'world'}

