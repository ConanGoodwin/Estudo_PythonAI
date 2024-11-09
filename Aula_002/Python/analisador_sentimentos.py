import gradio as gr
import google.generativeai as genai
import os
import time
from google.api_core.exceptions import InvalidArgument

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
prompt = """Você é um chatbot que analisa o sentimento de textos
fornecidos pelo usuário,incluindo arquivos de texto anexados.
não aceite arquivos que não sejam de texto.
O chatbot deve apenas ler o conteúdo textual dos arquivos. 
Exemplo de texto: 'Este é um texto de teste para análise de sentimento.'"""

model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=prompt)

chat = model.start_chat()
chat.send_message(
    "Olá, meu nome é conan, tudo bem?"
    "estou analisando sentimentos ligados a textos(incluindo anexados)."
)


def upload_files(message):
    file_paths = []

    if message["files"]:
        for file in message["files"]:
            uploaded_file = genai.upload_file(file["path"])
            while uploaded_file.state.name == "PROCESSING":
                time.sleep(3)
                uploaded_file = genai.upload_file(uploaded_file.name)
            file_paths.append(uploaded_file)

    return file_paths


def chat_gradio(message, _history):
    messageFiles = upload_files(message)
    respExtended = [message["text"]]

    respExtended.extend(messageFiles)
    chat.send_message(
        "Se você enviar uma imagem ou arquivo, sua resposta será descartada."
        "Responda apenas com texto. não aceite arquivos que não sejam de texto"
    )
    try:
        resp = chat.send_message(respExtended).text
    except InvalidArgument as e:
        resp = chat.send_message(
            f"O usuário te enviou um arquivo para você ler e obteve erro: {e}."
            "Pode explicar o que houve e dizer quais tipos de arquivos você "
            "dá suporte? Assuma que a pessoa não sabe programação e "
            "não quer o erro original. Explique de forma simples e concisa."
        ).text

    return resp


chat_interface = gr.ChatInterface(fn=chat_gradio, multimodal=True)
chat_interface.launch()
