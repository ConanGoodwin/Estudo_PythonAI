import gradio as gr
import google.generativeai as genai
import os
import time
from google.api_core.exceptions import InvalidArgument
from home_assistant import set_light_state, intruder_alert
from home_assistant import start_music, good_morning

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
initial_prompt = (
    "Você é um assistente virtual que pode controlar dispositivos domésticos."
    "Você tem acesso a funções que controlam a casa da pessoa que está usando."
    "Chame as funções quando achar que deve, mas nunca exponha o código delas."
    "Assuma que a pessoa é amigável e ajude-a a entender se algo der errado"
    "ou se você precisar de mais informações. Não esqueça de chamar as funções"
)
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    tools=[set_light_state, intruder_alert, start_music, good_morning],
    system_instruction=initial_prompt,
)

chat = model.start_chat(enable_automatic_function_calling=True)
chat.send_message(
    "Olá, tudo bem?"
    """estou rodando um codigo python que gerencia funções
    que alteram os estados de dispositivos de casa inteligente"""
)


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
            f"O usuário te enviou um arquivo para você ler e obteve erro: {e}."
            "Pode explicar o que houve e dizer quais tipos de arquivos você "
            "dá suporte? Assuma que a pessoa não sabe programação e "
            "não quer o erro original. Explique de forma simples e concisa."
        ).text

    return response


chat_interface = gr.ChatInterface(
    fn=gradio_chat, title="Assistente Inteligente 🏠", multimodal=True
)
chat_interface.launch()
