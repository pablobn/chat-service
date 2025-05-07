import openai
import os

# Asegúrate de tener la variable de entorno OPENAI_API_KEY definida
openai.api_key = os.getenv("OPENAI_API_KEY")

async def get_chatgpt_response(user_message: str) -> str:
    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-4o-mini",  # o usa "gpt-3.5-turbo" si lo prefieres
            messages=[
                {"role": "system", "content": "Eres un asistente útil en una sala de chat."},
                {"role": "user", "content": user_message}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error al llamar a ChatGPT: {e}")
        return "Lo siento, ha ocurrido un error al intentar responder con ChatGPT."
