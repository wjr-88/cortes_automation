# utils/transcriber.py

import whisper
import os


def transcrever_audio(video_path):
    """
    Extrai o áudio do vídeo e transcreve usando Whisper.
    Retorna dict com texto completo e segmentos.
    """

    print("🔊 Carregando modelo Whisper...")
    model = whisper.load_model("base")

    print("🧠 Transcrevendo áudio...")
    result = model.transcribe(video_path, language="pt")

    return {
        "text": result.get("text", ""),
        "segments": result.get("segments", [])
    }
