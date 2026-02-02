from pytube import YouTube
import os

def baixar_video(url, output_path="inputs/videos"):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
    return stream.download(output_path)
