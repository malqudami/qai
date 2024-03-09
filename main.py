from fastapi import FastAPI
from pydantic import BaseModel
from Modules import qai

app = FastAPI()

class message(BaseModel):
    role: str = 'user'
    content: str

@app.get("/")
def index():
    return "this is main page"

@app.get("/hc")
def health_check():
    return {"result": "Healthy"}

@app.post("/chat")
def chat(message: message):
    messages = [{
        "role": "system",
        "content": "this is to test openai"
    }]
    messages.append({"role": message.role, "content": message.content})

    response = qai.get_gpt_response(messages)
    return response