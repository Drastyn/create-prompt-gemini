from os import getenv, path, popen
import sys
import google.generativeai as genai

google_api_key = getenv('GOOGLE_API_KEY')
style = getenv('STYLE')
output_file_name = getenv('OUTPUT_FILE_NAME')

genai.configure(api_key=google_api_key)
context = "Tu objetivo principal es dado un texto generar una descripcion de un tatuaje que pueda ser introducida como prompt en un modelo texto a imagen. La desripcion debe ser concreta en no mas de 100 palabras y que pueda ser expresada mediante una imagen. El texto es: "
model = genai.GenerativeModel('gemini-pro')

def main():
    concept = checkInput(sys.argv)
    prompt  = context + concept
    response = model.generate_content(prompt).__getattribute__("text")
    popen(f"echo \"{style}\" > {output_file_name}")
    popen(f"echo \"{response}\" >> {output_file_name}")

def checkInput(arguments):
    arguments_length = len(arguments)
    prompt = ""
    if(arguments_length == 1 or arguments_length > 2):
        print("Recuerde ingresar solo un argumento")
        exit()
    if(path.isfile(arguments[1])):
        prompt = popen(f"cat {arguments[1]}").read().replace("\n", "\\n")
    else:
        prompt = arguments[1]
    return prompt

main()
