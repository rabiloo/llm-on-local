import requests

from fastapi import FastAPI, Form


app = FastAPI()
OLLAMA_URL = "http://localhost:11434/v1/chat/completions"


@app.post("/chatbot")
async def chatbot(
    model_alias: str = Form(default="llama3.2:1b"),
    question: str = Form(default=""),
):
    payload = {
        "model": model_alias,
        "messages": [{"role": "user", "content": question}],
        "temperature": 0.2,
    }
    response = requests.post(OLLAMA_URL, json=payload).json()

    if response.get("choices") is None:
        return response["error"].get("message", "Error: No response from Ollama.")

    return response["choices"][0]["message"].get("content", "Error: No response from Ollama.")
