def aplicar_regras_audio(
    clip,
    video_tipo,
    narracao_path=None,
    musica_path=None
):
    """
    highlights  -> remove áudio original, adiciona música + narração
    commentary  -> mantém áudio original, sem narração
    """

    if video_tipo == "highlights":
        # Remove áudio original
        clip = clip.without_audio()

        audio_tracks = []

        if musica_path:
            audio_tracks.append(musica_path)

        if narracao_path:
            audio_tracks.append(narracao_path)

        return clip, audio_tracks

    if video_tipo == "commentary":
        # Mantém áudio original
        return clip, []

    raise ValueError("Tipo de vídeo inválido")
