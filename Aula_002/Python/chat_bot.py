import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

chat = model.start_chat()
resp = chat.send_message("Olá")
print(resp.text)
