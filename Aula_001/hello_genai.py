import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

resp = model.generate_content(
    "Crie um historia sobre um computador mágico."
  )

print(resp.text)
