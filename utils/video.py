from moviepy.editor import (
    CompositeVideoClip,
    TextClip,
    AudioFileClip,
    CompositeAudioClip
)

def criar_short(
    clip,
    output_path,
    audio_tracks=None,
    titulo="Cruzeiro hoje ⚽"
):
    layers = [clip]

    texto = TextClip(
        titulo,
        fontsize=60,
        color="white",
        method="caption",
        size=(900, None)
    ).set_position(("center", "top")).set_duration(clip.duration)

    layers.append(texto)

    if audio_tracks:
        audios = [AudioFileClip(a).set_duration(clip.duration) for a in audio_tracks]
        audio_final = CompositeAudioClip(audios)
        clip = clip.set_audio(audio_final)

    final = CompositeVideoClip(layers)
    final.write_videofile(output_path, fps=30)
