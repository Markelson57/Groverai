import asyncio
from asyncio_mqtt import Client, MqttError

class MQTTClient:
    def __init__(self, broker="broker.hivemq.com", port=1883, topic="isa_topic"):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client = Client(self.broker, self.port)

    async def connect(self):
        try:
            await self.client.connect()
            print("[MQTT conectado]")
        except MqttError as e:
            print(f"[MQTT error]: {e}")

    async def subscribe(self, callback):
        async with self.client.unfiltered_messages() as messages:
            await self.client.subscribe(self.topic)
            async for message in messages:
                await callback(message.topic, message.payload.decode())

    async def publish(self, msg):
        try:
            await self.client.publish(self.topic, msg)
        except MqttError as e:
            print(f"[MQTT publish error]: {e}")
