import openai

# Configura tu clave API de OpenAI, recordar instalar version pip install openai == 0.28
openai.api_key = "Escribe aqui el token"

# Texto de entrada para generar continuación
input_text = '¿Quién es Leonel Messi?'

chat_completion = openai.ChatCompletion.create(
    model = "gpt-4-0125-preview",
    messages=[{"role":"user","content":input_text}]
)

response = chat_completion['choices'][0]['message']['content']

print(response)
