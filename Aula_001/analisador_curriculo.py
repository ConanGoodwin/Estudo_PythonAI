import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

with open("curriculo_int_conan.txt", "r") as f:
    curriculo = f.read()

prompt = f"""
  Por favor, aprimore o meu currículo para deixá-lo mais assertivo
  e enfatizando os pontos positivos. Eis o meu currículo: {curriculo}
"""
resp = model.generate_content(prompt)

print(resp.text)
