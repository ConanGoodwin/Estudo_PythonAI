import google.generativeai as genai
from google.api_core.exceptions import InvalidArgument
import os
import gradio as gr
import time
from home_ass_rev import set_light_state, start_music

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]

genai.configure(api_key=GEMINI_API_KEY)
initial_prompt = (
    "Você é um assistente virtual que pode controlar dispositivos domésticos. "
    "Você tem acesso a funções que controlam a casa da pessoa que está usando."
    "Chame as funções quando achar que deve, mas nunca exponha o código delas."
    "Assuma que a pessoa é amigável e ajude-a a entender o que aconteceu "
    "se algo der errado ou se você precisar de mais informações."
    "Não esqueça de, de fato, chamar as funções."
)
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    tools=[set_light_state, start_music],
    system_instruction=initial_prompt,
)

chat = model.start_chat(enable_automatic_function_calling=True)


def assemble_prompt(message):
    prompt = [message["text"]]
    uploaded_files = upload_file(message)
    # prompt.extend(uploaded_files)

    return prompt


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
    prompt = assemble_prompt(message)

    try:
        response = chat.send_message(prompt)
    except InvalidArgument as e:
        response = chat.send_message(
            f"O usuário te enviou um arquivo para você ler e obteve erro: {e}."
            "Pode explicar o que houve e dizer quais tipos de arquivos você "
            "dá suporte? Assuma que a pessoa não sabe programação e "
            "não quer o erro original. Explique de forma simples e concisa."
        )

    return response.text


chat_interface = gr.ChatInterface(
    fn=gradio_chat, title="Assistente Inteligente 🏠", multimodal=True
)

chat_interface.launch()
