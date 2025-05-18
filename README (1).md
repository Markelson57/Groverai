
# ISA Project - Asistente Inteligente Avanzado

![ISA Logo](https://your-logo-link-here.com/logo.png)

---

## Descripción

ISA es un asistente inteligente avanzado, modular y extensible, diseñado para funcionar en tiempo real con interacción por voz, integración IoT, gestión de memoria contextual, y capacidades de razonamiento y fusión de respuestas IA basadas en OpenAI GPT.

Este proyecto está pensado para desarrolladores que quieren construir un asistente de voz potente con soporte para MQTT, memoria a corto y largo plazo, y una arquitectura asíncrona y escalable.

---

## Características principales

- **Reconocimiento y síntesis de voz:** Wake word personalizado, comandos por voz y respuestas habladas.
- **Motor de fusión de respuestas:** Uso de GPT-4o-mini con contexto histórico.
- **Gestión avanzada de memoria:** Memoria a corto y largo plazo con SQLite y memoria vectorial con FAISS.
- **Integración IoT vía MQTT:** Control y comunicación con dispositivos conectados.
- **Arquitectura modular:** Fácil ampliación con nuevos módulos de razonamiento y capacidades.
- **Código asíncrono:** Eficiencia y escalabilidad con asyncio en Python.

---

## Estructura del proyecto

```
/isa_project
├── main.py                  # Código central que enlaza todo
├── core.py                  # Núcleo modular y sistema de eventos async
├── voice_io.py              # Módulo para síntesis y reconocimiento de voz
├── fusion_engine.py         # Motor de fusión de respuestas IA
├── memory.py                # Gestión de memoria y contexto
├── reasoning_modules.py     # Módulos individuales de IA y lógica
├── mqtt_client.py           # Integración MQTT / IoT
├── vector_memory.py         # Memoria vectorial FAISS (avanzado)
└── utils.py                 # Funciones utilitarias generales
```

---

## Requisitos

- Python 3.9+
- Dependencias de Python:
  ```bash
  pip install asyncio pyttsx3 SpeechRecognition vosk pyaudio openai asyncio-mqtt faiss-cpu numpy
  ```
- Modelo Vosk para reconocimiento de voz [descargar aquí](https://alphacephei.com/vosk/models)
- Clave API de OpenAI (configurar en `fusion_engine.py`)

---

## Instalación y configuración

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/isa_project.git
   cd isa_project
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Descarga y coloca el modelo Vosk en la carpeta `/isa_project/model`

4. Abre `fusion_engine.py` y reemplaza `"TU_API_KEY"` con tu clave real de OpenAI.

5. Ejecuta el asistente:
   ```bash
   python main.py
   ```

---

## Uso

- Di el wake word configurado (por defecto "isa").
- Habla tu comando o pregunta.
- ISA responderá de forma hablada y contextual.
- También puede interactuar con dispositivos IoT mediante MQTT.

---

## Cómo contribuir

¡Contribuciones bienvenidas!

- Reporta bugs o abre pull requests en GitHub.
- Añade nuevos módulos de razonamiento o mejora la memoria.
- Optimiza el reconocimiento o la síntesis de voz.

---

## Licencia

Este proyecto está bajo licencia MIT.

---

## Contacto

Markelson - YouTuber / Streamer / Programador  
Correo: tuemail@ejemplo.com  
GitHub: [github.com/markelson57](https://github.com/markelson57)

---

¡Gracias por usar ISA! 🚀

---

## API Key OpenAI

Para obtener la API Key de OpenAI ChatGPT, visita:
https://platform.openai.com/account/api-keys
