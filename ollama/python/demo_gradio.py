import gradio as gr
import requests

OLLAMA_URL = "http://localhost:11434/v1/chat/completions"
MODEL_NAME = "llama3.2:1b"


def chatbot(message, history):
    payload = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": message}],
    }
    response = requests.post(OLLAMA_URL, json=payload)
    reply = response.json()["choices"][0]["message"].get("content", "Error: No response from Ollama.")
    history.append((message, reply))
    return "", history


with gr.Blocks() as demo:
    with gr.Tab("Chatbot"):
        gr.Markdown(value="## Ollama Chatbot")
        with gr.Row():
            with gr.Column():
                msg = gr.Textbox(placeholder="Type your message...")
                btn = gr.Button("Send")
            chatbot_box = gr.Chatbot(height=800)

        btn.click(chatbot, inputs=[msg, chatbot_box], outputs=[msg, chatbot_box])

demo.launch(server_name="0.0.0.0", server_port=7860, share=True)
