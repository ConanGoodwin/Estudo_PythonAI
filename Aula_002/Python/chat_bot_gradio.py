import google.generativeai as genai
import gradio as gr
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

chat = model.start_chat()


def gradio_chat(message, _history):
    response = chat.send_message(message).text
    return response


chat_interface = gr.ChatInterface(gradio_chat)
chat_interface.launch()
