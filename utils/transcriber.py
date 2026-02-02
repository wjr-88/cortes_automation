import whisper

model = whisper.load_model("base")

def transcrever_video(audio_path):
    result = model.transcribe(audio_path, language="pt")
    return result["segments"]
