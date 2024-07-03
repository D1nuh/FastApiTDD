from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def test():
  return {"TesteTDD": "Este é um exemplo de codigo TDD"}
