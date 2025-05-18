import asyncio
import openai

from api.env import API_KEY  # Sustituye con tu API Key

openai.api_key = API_KEY  # Sustituye con tu API Key

class FusionEngine:
    def __init__(self):
        pass

    async def openai_query(self, prompt, context):
        context_str = "\n".join([f"Tú: {c[0]}\nISA: {c[1]}" for c in context[-5:]])
        full_prompt = f"{context_str}\nTú: {prompt}\nISA:"

        try:
            response = await asyncio.to_thread(
                lambda: openai.Completion.create(
                    engine="gpt-4o-mini",
                    prompt=full_prompt,
                    max_tokens=150,
                    temperature=0.7,
                    n=1,
                    stop=["\nTú:", "\nISA:"]
                )
            )
            answer = response.choices[0].text.strip()
            return answer
        except Exception as e:
            print(f"[Error OpenAI]: {e}")
            return None

    async def fallback_local(self, prompt):
        # Respuesta simple para fallback local si no hay conexión OpenAI
        return f"Lo siento, no puedo procesar eso ahora: {prompt}"

    async def get_response(self, prompt, context):
        answer = await self.openai_query(prompt, context)
        if answer is None:
            answer = await self.fallback_local(prompt)
        return answer
