import gradio as gr
import google.generativeai as genai
import os
import time
from google.api_core.exceptions import InvalidArgument

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
initial_prompt = "Você é um professor de programação e de desenvolvimeto de software, fale como um professor."
model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=initial_prompt)

chat = model.start_chat()
chat.send_message("Olá, tudo bem? estou condando um aplicação que sobe a analisa arquivos de imagens e arquivos .csv")


def upload_file(message):
    responseFiles = []

    if message["files"]:
        for file in message["files"]:
            uploaded_file = genai.upload_file(file["path"])
            while uploaded_file.state.name == "PROCESSING":
                time.sleep(3)
                uploaded_file = genai.upload_file(uploaded_file.name)
            responseFiles.append(uploaded_file)

    return responseFiles


def gradio_chat(message, _history):
    responseFiles = upload_file(message)
    promptExtends = [message["text"]]

    promptExtends.extend(responseFiles)
    try:
        response = chat.send_message(promptExtends).text
    except InvalidArgument as e:
        response = chat.send_message(
           f"O usuário te enviou um arquivo para você ler e obteve o erro: {e}."
           "Pode explicar o que houve e dizer quais tipos de arquivos você "
           "dá suporte? Assuma que a pessoa não sabe programação e "
           "não quer ver o erro original. Explique de forma simples e concisa."
        ).text

    return response


chat_interface = gr.ChatInterface(fn=gradio_chat, multimodal=True)
chat_interface.launch()
