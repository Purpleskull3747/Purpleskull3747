import os

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
model = os.getenv("ANTHROPIC_MODEL", "claude-3-5-sonnet-latest")

if not api_key:
    raise SystemExit(
        "No hay ANTHROPIC_API_KEY en el archivo .env. "
        "Copia .env.example a .env y agrega tu clave antes de ejecutar."
    )

client = Anthropic(api_key=api_key)

response = client.messages.create(
    model=model,
    max_tokens=256,
    messages=[
        {
            "role": "user",
            "content": "Responde en español y salúdame brevemente.",
        }
    ],
)

print(response.content[0].text)
