from moviepy import VideoFileClip
from config import SHORT_DURATION

def cortar_trecho(video_path, inicio=10):
    clip = VideoFileClip(video_path)
    fim = inicio + SHORT_DURATION
    return clip.subclip(inicio, fim)
