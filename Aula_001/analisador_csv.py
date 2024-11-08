import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

students_spreadsheet = genai.upload_file(
    path="desempenho_estudantes_enem.csv",
    display_name="Notas do Enem"
  )

prompt = """Pode gerar um relatório de dois ou três parágrafos
  baseado nesses dados?
  Fale de tendências nos grupos de estudantes."""

resp = model.generate_content(
    [prompt, students_spreadsheet]
  )

print(resp.text)
