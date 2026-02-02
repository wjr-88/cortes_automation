from gtts import gTTS
from moviepy import AudioFileClip
import json
import os

def gerar_roteiro():
    with open("roteiros/cruzeiro.json", "r", encoding="utf-8") as f:
        ctx = json.load(f)

    texto = f"""
Esse jogo mostrou exatamente o momento do Cruzeiro.
{ctx['analise']}
A torcida segue {ctx['emocao']}.
E você, confia nesse time?
"""
    return texto.strip()


def gerar_narracao(texto, output="outputs/audios/narracao.mp3"):
    os.makedirs("outputs/audios", exist_ok=True)
    tts = gTTS(text=texto, lang="pt", slow=False)
    tts.save(output)
    return output
