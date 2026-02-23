import asyncio
import pyttsx3
import speech_recognition as sr
import vosk
import pyaudio
import json

class VoiceIO:
    def __init__(self, wake_word="Grover"):
        self.wake_word = wake_word.lower()
        self.tts_engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.vosk_model = vosk.Model("model")  # Ruta al modelo vosk
        self.vosk_recognizer = vosk.KaldiRecognizer(self.vosk_model, 16000)
        self.pyaudio_instance = pyaudio.PyAudio()
        self.stream = None

    def say(self, text):
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

    async def listen_wake_word(self):
        if self.stream is None:
            self.stream = self.pyaudio_instance.open(format=pyaudio.paInt16,
                                                     channels=1,
                                                     rate=16000,
                                                     input=True,
                                                     frames_per_buffer=4000)
            self.stream.start_stream()
        print("[👂 Escuchando wake word...]")
        while True:
            data = self.stream.read(4000, exception_on_overflow=False)
            if self.vosk_recognizer.AcceptWaveform(data):
                result = json.loads(self.vosk_recognizer.Result())
                text = result.get("text", "").lower()
                if self.wake_word in text:
                    print("[Wake word detectado]")
                    return True
            await asyncio.sleep(0.1)

    async def listen_command(self, timeout=5):
        with sr.Microphone() as source:
            print("[🎙️ Escuchando comando...]")
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source, timeout=timeout)
                text = self.recognizer.recognize_google(audio, language="es-ES")
                print(f"[Comando recibido]: {text}")
                return text.lower()
            except sr.WaitTimeoutError:
                print("[Timeout escuchando comando]")
                return None
            except sr.UnknownValueError:
                print("[No se entendió el comando]")
                return None
            except sr.RequestError as e:
                print(f"[Error servicio voz]: {e}")
                return None

