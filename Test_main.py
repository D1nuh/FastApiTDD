from fastapi.testclient import TestClient
from main import app

cliente = TestClient(app)

def teste_raiz():
    resposta = cliente.get("/")
    assert resposta.status_code == 200
    assert resposta.json() == {"TesteTDD": "Este é um exemplo de codigo TDD"}

