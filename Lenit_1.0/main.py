import threading
import time
import telebot

from config import Chat_id, Token, url
from formatos_de_texto import info as texto_info, ayuda, inicio
from scraper import obtener_info, obtener_ruta
from modelo import respuesta_ai

bot = telebot.TeleBot(Token)

# Cargamos el contexto obtenido por scraping al inicio (esto sirve de base de conocimiento para el modelo de IA)
info_context = obtener_info()

# Comando /ayuda
@bot.message_handler(commands=["ayuda"])
def responder_ayuda(message):
    bot.reply_to(message, ayuda())

# Comando /docs
@bot.message_handler(commands=["docs"])
def responder_docs(message):
    bot.reply_to(message, url)

# Comando /info: Muestra parte del contenido scrapeado de la documentación de Python
@bot.message_handler(commands=["info"])
def responder_info(message):
    bot.send_chat_action(message.chat.id, "typing")
    time.sleep(2)
    bot.reply_to(message, info_context)

# Comando /ruta: Muestra la ruta de aprendizaje con enlaces a los temas
@bot.message_handler(commands=["ruta"])
def dar_ruta(message):
    bot.send_chat_action(message.chat.id, "typing")
    time.sleep(1)
    bot.reply_to(message, obtener_ruta(), disable_web_page_preview=True)

# Comando /pregunta: El usuario escribe una pregunta y el modelo de IA busca la respuesta en el contexto
@bot.message_handler(commands=["pregunta"])
def responder_pregunta(message):
    # Se extrae la pregunta eliminando el comando
    pregunta = message.text[len("/pregunta"):].strip()
    if not pregunta:
        bot.reply_to(message, "Por favor, escribe tu pregunta después del comando /pregunta.")
        return
    bot.send_chat_action(message.chat.id, "typing")
    respuesta = respuesta_ai(pregunta, info_context)
    bot.reply_to(message, respuesta)

# Respuesta a mensajes de texto que no sean comandos
@bot.message_handler(content_types=["text"])
def responder_mensajes(message):
    if message.text.lower() == "qué hago?":
        bot.send_message(message.chat.id, texto_info())
    else:
        bot.send_message(message.chat.id, inicio())

# Función que se encarga de recibir mensajes en un bucle infinito
def recibir_mensajes():
    bot.infinity_polling()

# Punto de entrada principal
if __name__ == "__main__":
    hilo_bot = threading.Thread(name="Hilo_bot", target=recibir_mensajes)
    hilo_bot.start()
    bot.send_message(
        Chat_id,
        "Hola, esta es una primera versión de prueba de <b><i><u>Lenit</u></i></b>. ¿En qué puedo ayudarte?",
        parse_mode="html",
    )


