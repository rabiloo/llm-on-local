import json

import gradio as gr
import requests

VLLM_URL = "http://localhost:8000/v1/chat/completions"
HEADERS = {"Content-Type": "application/json"}
MODEL_NAME = "Qwen/Qwen2-1.5B-Instruct"


def chat_with_llm(message, history):
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    if history:
        for user_msg, bot_reply in history:
            messages.append({"role": "user", "content": user_msg})
            messages.append({"role": "assistant", "content": bot_reply})

    # Append the latest user message
    messages.append({"role": "user", "content": message})

    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "temperature": 0.2,
    }

    response = requests.post(VLLM_URL, headers=HEADERS, data=json.dumps(payload)).json()
    if response.get("choices") is None:
        return response["error"].get("message", "Error: No response from Ollama.")

    return response["choices"][0]["message"].get("content", "Error: No response from Ollama.")


gr.ChatInterface(fn=chat_with_llm, title="vLLM Chatbot").launch(share=True)
