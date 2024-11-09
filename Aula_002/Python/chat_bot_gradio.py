import google.generativeai as genai
import gradio as gr
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
initial_prompt = "Você é um professor de programação e de desenvolvimeto de software, fale como um professor."
model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=initial_prompt)

chat = model.start_chat()


def gradio_chat(message, _history):
    response = chat.send_message(message).text
    return response


chat_interface = gr.ChatInterface(gradio_chat)
chat_interface.launch()
