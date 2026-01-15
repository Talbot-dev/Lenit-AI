# formatos_de_texto.py
def info() -> str:
    return (
        "Pide una ruta de aprendizaje con los temas ordenados de manera secuencial con el comando /ruta.\n\n"
        "O también conoce más funciones a través del comando /ayuda"
    )

def ayuda() -> str:
    return (
        "Aquí tienes más funcionalidades:\n\n"
        "El comando /docs: Te dará el enlace a la documentación oficial de python.\n\n"
        "El comando /info: Te dará una descripción y contexto sobre qué es python.\n"
    )

def inicio() -> str:
    return (
        "Actualmente no puedo procesar mensajes autónomos, pero puedo darte una orientación de como ayudar siempre que escribas:\n\n"
        " 'Qué hago?' "
    )