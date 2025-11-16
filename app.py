from google import genai
import os
from groq import Groq

client_gemini = genai.Client()
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)



perguntas = ""

#PERGUNTAS
with open("perguntas.txt", 'r', encoding='utf-8') as arquivo:
        # O método .read() lê todo o conteúdo para uma única string
        perguntas = arquivo.read()

#LLMS
response_gemini = client_gemini.models.generate_content(
    model="gemini-2.5-flash",
    contents=perguntas,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": perguntas,
        }
    ],
    model="llama-3.3-70b-versatile",
)


#RESPOSTAS
with open("respostas-gemini.json", 'w', encoding='utf-8') as arquivo:
        # O método .write() escreve a string no arquivo.
        # Você deve adicionar manualmente o caractere de quebra de linha ('\n').
        arquivo.write(response_gemini.text)

with open("respostas-groq.json", 'w', encoding='utf-8') as arquivo:
        # O método .write() escreve a string no arquivo.
        # Você deve adicionar manualmente o caractere de quebra de linha ('\n').
        arquivo.write(chat_completion.choices[0].message.content)














