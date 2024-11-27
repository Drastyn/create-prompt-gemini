from os import getenv, path, popen
import sys
import google.generativeai as genai


GOOGLE_API_KEY = getenv('GOOGLE_API_KEY')
OUTPUT_FILE_NAME = getenv('OUTPUT_FILE_NAME')


genai.configure(api_key=GOOGLE_API_KEY)
context = "Tu objetivo principal es, dado un concepto y un estilo, generar una descripción de un tatuaje que pueda ser introducida como prompt en un modelo texto a imagen. La descripción debe ser concreta en no más de 100 palabras y que pueda ser expresada mediante una imagen. "
model = genai.GenerativeModel('gemini-pro')


def main():
    prompt = prepare_prompt(sys.argv)
    prompt = context + prompt
    response = model.generate_content(prompt).__getattribute__("text")
    popen(f"echo \"{response}\" >> {OUTPUT_FILE_NAME}")


def prepare_prompt(arguments):
    concept = arguments[1]
    style = arguments[2]
    prompt = f"Concepto: {concept}, Estilo: {style}"
    return prompt


main()
