# Aquí puedes añadir módulos especializados de razonamiento
# Por ejemplo, módulos para análisis de sentimientos, lógica, control domótico, etc.

class ReasoningModules:
    def __init__(self):
        pass

    def analyze_sentiment(self, text):
        # Ejemplo básico de análisis de sentimiento
        positive_words = ['bien', 'genial', 'bueno', 'excelente', 'positivo']
        negative_words = ['mal', 'malo', 'triste', 'negativo', 'pésimo']

        score = 0
        text_lower = text.lower()
        for pw in positive_words:
            if pw in text_lower:
                score += 1
        for nw in negative_words:
            if nw in text_lower:
                score -= 1

        if score > 0:
            return "Positivo"
        elif score < 0:
            return "Negativo"
        else:
            return "Neutral"
