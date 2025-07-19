import openai

openai.api_key = 'your-api-key-here'

def generate_blog(tema):
    respuesta = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un experto en redacción de blogs."},
            {"role": "user", "content": f"Escribe un blog sobre {tema}"}
        ],
        max_tokens=100,
        temperature=0.7
    )
    blog_creado = respuesta.choices[0].message.content.strip()
    return blog_creado

print(generate_blog("La importancia de la inteligencia artificial en la educación"))