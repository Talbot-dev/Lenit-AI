from transformers import pipeline

# Inicializo el pipeline de QA con un modelo ligero
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

def respuesta_ai(pregunta, contexto):
    """
    Recibe la pregunta y el contexto (texto largo obtenido por scraping)
    y divide el contexto en fragmentos (chunks) para obtener la respuesta
    con mayor score.
    """
    # Separo el contexto en chunks basados en párrafos
    chunks = contexto.split("\n\n")
    best_answer = None
    best_score = 0

    for chunk in chunks:
        try:
            result = qa_pipeline(question=pregunta, context=chunk)
            if result["score"] > best_score:
                best_score = result["score"]
                best_answer = result["answer"]
        except Exception as e:
            continue

    if best_answer:
        return best_answer
    else:
        return "Lo siento, no encontré una respuesta a tu pregunta."