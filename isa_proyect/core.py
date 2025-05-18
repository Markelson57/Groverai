import asyncio
from memory import MemoryManager
from fusion_engine import FusionEngine
from voice_io import VoiceIO
from mqtt_client import MQTTClient

class Core:
    def __init__(self):
        self.memory = MemoryManager()
        self.fusion = FusionEngine()
        self.voice_io = VoiceIO()
        self.mqtt_client = MQTTClient()
        self.event_queue = asyncio.Queue()
        self.running = True

    async def process_event(self, event):
        if event['type'] == 'wake_word':
            self.voice_io.say("¿En qué puedo ayudarte?")
            command = await self.voice_io.listen_command()
            if command:
                context = self.memory.get_short_term()
                answer = await self.fusion.get_response(command, context)
                self.memory.add_short_term(command, answer)
                self.voice_io.say(answer)

        elif event['type'] == 'mqtt_msg':
            # Aquí procesar mensajes MQTT si quieres hacer algo
            print(f"[MQTT mensaje]: {event['data']}")

    async def event_loop(self):
        await self.mqtt_client.connect()
        asyncio.create_task(self.mqtt_client.subscribe(self.mqtt_callback))
        asyncio.create_task(self._wake_word_listener())

        while self.running:
            event = await self.event_queue.get()
            await self.process_event(event)

    async def mqtt_callback(self, topic, payload):
        await self.event_queue.put({'type': 'mqtt_msg', 'data': payload})

    async def _wake_word_listener(self):
        while self.running:
            detected = await self.voice_io.listen_wake_word()
            if detected:
                await self.event_queue.put({'type': 'wake_word'})
