import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

dog_image_01 = genai.upload_file(
    path="cachorro_collie_acho.png",
    display_name="dog"
  )

dog_image_02 = genai.upload_file(
    path="cachorro_golden_retriever.png",
    display_name="dog"
  )

prompt = """
  Pode identificar a raça do cachorro da foto
  e me dar duas ou três frases de informações a respeito dele?
  De preferência, alguma curiosidade interessante em português,
  citando a fonte da informação e sempre de um jeito leve e interessante.
"""

resp = model.generate_content(
    [prompt, dog_image_01]
  )

print(resp.text)

resp = model.generate_content(
    [prompt, dog_image_02]
  )

print(resp.text)
