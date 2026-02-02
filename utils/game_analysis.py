# utils/game_analysis.py

def analisar_contexto(segmentos):
    """
    Analisa os textos transcritos e extrai sinais do jogo
    """
    sinais = {
        "gol": 0,
        "pressao": 0,
        "chance": 0,
        "final": 0
    }

    for seg in segmentos:
        texto = seg["text"].lower()

        if "gol" in texto:
            sinais["gol"] += 1

        if any(p in texto for p in ["pressiona", "pressão", "sufoco"]):
            sinais["pressao"] += 1

        if any(c in texto for c in ["chance", "quase", "perdeu"]):
            sinais["chance"] += 1

        if any(f in texto for f in ["final", "últimos minutos", "acréscimos"]):
            sinais["final"] += 1

    return sinais


def interpretar_jogo(sinais):
    """
    Interpreta o contexto geral do jogo a partir dos sinais
    """
    if sinais["gol"] >= 2 and sinais["pressao"] == 0:
        return "vitória controlada"

    if sinais["gol"] >= 1 and sinais["pressao"] >= 1:
        return "vitória sofrida"

    if sinais["gol"] == 0 and sinais["pressao"] >= 2:
        return "pressão sem resultado"

    return "jogo equilibrado"
