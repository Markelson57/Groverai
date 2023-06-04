
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.chat.util import Chat, reflections
import os
import sqlite3
import subprocess

# Limpiar pantalla
def limpiar_pantalla():
    subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)

# Instalar paquetes necesarios
def instalar_paquetes():
    paquetes = ['nltk']

    for paquete in paquetes:
        subprocess.call(f'pip install {paquete}', shell=True)

# Descargar recursos necesarios para el procesamiento del lenguaje natural
def descargar_recursos_nltk():
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')

# Verificar si los paquetes necesarios están instalados
def verificar_paquetes_instalados():
    paquetes = ['nltk']

    paquetes_faltantes = []
    for paquete in paquetes:
        try:
            __import__(paquete)
        except ImportError:
            paquetes_faltantes.append(paquete)
    
    return paquetes_faltantes

# Verificar si los recursos de nltk están descargados
def verificar_recursos_nltk_descargados():
    recursos = ['punkt', 'stopwords', 'wordnet']

    recursos_faltantes = []
    for recurso in recursos:
        if not nltk.corpus.reader.is_corpus_file_present(recurso):
            recursos_faltantes.append(recurso)
    
    return recursos_faltantes

# Función para limpiar y lematizar el texto de entrada
def limpiar_texto(texto):
    tokens = word_tokenize(texto.lower())
    stopwords_esp = set(stopwords.words('spanish'))
    tokens_filtrados = [lemmatizer.lemmatize(token) for token in tokens if token.isalnum() and token not in stopwords_esp]
    texto_limpiado = ' '.join(tokens_filtrados)
    return texto_limpiado

# Pares de preguntas y respuestas para el chatbot
pares_grover = {
    'en': [
        [
            r"my name is (.*)",
            ["Hello %1, How can I help you today?",]
        ],
        [
            r"how are you ?",
            ["I'm doing well, thank you! How about you?",]
        ],
        [
            r"what (.*) do you want ?",
            ["I'm here to help you. You can ask questions or present problems.",]
        ],
        [
            r"how can I (.*)",
            ["You can try %1 by following these steps: [Recommended steps].",]
        ],
        [
            r"bye",
            ["Goodbye. Have a great day!",]
        ],
        [
            r"(.*)",
            ["I'm not sure, can you be more specific?",]
        ]
    ],
    'fr': [
        [
            r"je m'appelle (.*)",
            ["Bonjour %1, comment puis-je vous aider ?",]
        ],
        [
            r"comment ça va ?",
            ["Je vais bien, merci ! Et vous ?",]
        ],
        [
            r"que (.*) veux-tu ?",
            ["Je suis là pour vous aider. Vous pouvez poser des questions ou présenter des problèmes.",]
        ],
        [
            r"comment puis-je (.*)",
            ["Vous pouvez essayer %1 en suivant ces étapes : [Étapes recommandées].",]
        ],
        [
            r"au revoir",
            ["Au revoir. Passez une excellente journée !",]
        ],
        [
            r"(.*)",
            ["Je ne suis pas sûr, pouvez-vous être plus précis ?",]
        ]
    ],
    'es': [
        [
            r"mi nombre es (.*)",
            ["Hola %1, ¿en qué puedo ayudarte hoy?",]
        ],
        [
            r"cómo estás ?",
            ["¡Estoy bien, gracias! ¿Y tú?",]
        ],
        [
            r"qué (.*) quieres ?",
            ["Estoy aquí para ayudarte. Puedes hacer preguntas o plantear problemas.",]
        ],
        [
            r"cómo puedo (.*)",
            ["Puedes intentar %1 siguiendo estos pasos: [Pasos recomendados].",]
        ],
        [
            r"adiós",
            ["Adiós. ¡Que tengas un excelente día!",]
        ],
        [
            r"(.*)",
            ["No estoy seguro, ¿puedes ser más específico?",]
        ]
    ]
}

# Inicializar el lematizador de palabras
lemmatizer = WordNetLemmatizer()

# Verificar paquetes instalados
paquetes_faltantes = verificar_paquetes_instalados()
if paquetes_faltantes:
    print("Faltan paquetes necesarios. Instalando...")
    instalar_paquetes()

# Verificar recursos de nltk descargados
recursos_faltantes = verificar_recursos_nltk_descargados()
if recursos_faltantes:
    print("Faltan recursos de nltk. Descargando...")
    descargar_recursos_nltk()

# Función para obtener una respuesta del chatbot Grover
def obtener_respuesta_grover(entrada, idioma):
    entrada_limpia = limpiar_texto(entrada)
    respuesta = grover.respond(entrada_limpia)
    return respuesta

# Función para crear una cuenta de usuario
def crear_cuenta():
    correo = input("Ingrese su correo electrónico: ")
    contrasena = input("Ingrese su contraseña: ")
    confirmar_contrasena = input("Confirme su contraseña: ")

    if contrasena == confirmar_contrasena:
        conn = sqlite3.connect('usuarios.db')
        c = conn.cursor()
        c.execute("INSERT INTO usuarios VALUES (?, ?)", (correo, contrasena))
        conn.commit()
        conn.close()
        print("Cuenta creada exitosamente.")
    else:
        print("Las contraseñas no coinciden. Vuelva a intentarlo.")

# Función para iniciar sesión
def iniciar_sesion():
    correo = input("Ingrese su correo electrónico: ")
    contrasena = input("Ingrese su contraseña: ")

    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios WHERE correo=? AND contrasena=?", (correo, contrasena))
    resultado = c.fetchone()
    conn.close()

    if resultado:
        print("Inicio de sesión exitoso.")
        return True
    else:
        print("Inicio de sesión inválido.")
        return False

# Función principal del programa
def main():
    # Limpiar pantalla
    limpiar_pantalla()

    print("**********************************")
    print("*           GROVER CHAT          *")
    print("**********************************")
    print("Bienvenido al programa simulador de asistente virtual Grover.")

    # Verificar si hay usuarios en la base de datos
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute("SELECT count(*) FROM usuarios")
    resultado = c.fetchone()
    conn.close()

    if resultado[0] == 0:
        print("No hay usuarios registrados. Por favor, cree una cuenta para continuar.")
        crear_cuenta()

    while True:
        limpiar_pantalla()
        print("**********************************")
        print("*           GROVER CHAT          *")
        print("**********************************")
        print("Por favor, elija una opción:")
        print("1. Iniciar sesión")
        print("2. Crear cuenta")
        print("3. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            # Iniciar sesión
            if iniciar_sesion():
                limpiar_pantalla()
                print("**********************************")
                print("*           GROVER CHAT          *")
                print("**********************************")
                print("Inicio de sesión exitoso. ¡Bienvenido a Grover Chat!")
                print("Puedes comenzar a hacer preguntas o escribir 'adiós' para salir.")
                print("**********************************")

                while True:
                    entrada = input("(Usuario): ")
                    if entrada.lower() == "adiós":
                        confirmacion = input("¿Estás seguro de que quieres salir? (S/N): ")
                        if confirmacion.lower() == "s":
                            break
                    respuesta = obtener_respuesta_grover(entrada, idioma)
                    print("Grover: " + respuesta)
            else:
                print("El inicio de sesión no fue válido. Intenta nuevamente.")
        elif opcion == "2":
            # Crear cuenta
            crear_cuenta()
        elif opcion == "3":
            # Salir del programa
            confirmacion = input("¿Estás seguro de que quieres salir? (S/N): ")
            if confirmacion.lower() == "s":
                limpiar_pantalla()
                print("Gracias por utilizar Grover Chat. ¡Hasta luego!")
                break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")

# Ejecutar el programa
if __name__ == '__main__':
    main()
