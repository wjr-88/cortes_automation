import os

from utils.downloader import baixar_video
from utils.cutter import cortar_trecho
from utils.transcriber import transcrever_video
from utils.game_analysis import extrair_sinais, interpretar_jogo
from utils.script_generator import gerar_roteiro
from utils.narration import gerar_narracao
from utils.audio_rules import aplicar_regras_audio
from utils.video import criar_short


# ============================
# CONFIGURAÇÕES GERAIS
# ============================

MUSICA_PADRAO = "inputs/musicas/musica1.mp3"

PASTA_AUDIOS = "outputs/audios"
PASTA_SHORTS = "outputs/shorts"

os.makedirs(PASTA_AUDIOS, exist_ok=True)
os.makedirs(PASTA_SHORTS, exist_ok=True)


# ============================
# EXECUÇÃO PRINCIPAL
# ============================

if __name__ == "__main__":

    print("\n=== GERADOR DE VÍDEOS - CRUZEIRO ===\n")

    # --------------------------------
    # Entrada do usuário
    # --------------------------------
    url = input("Cole o link do vídeo do YouTube: ").strip()

    video_tipo = input(
        "Tipo de vídeo? (highlights / commentary): "
    ).strip().lower()

    if video_tipo not in ["highlights", "commentary"]:
        raise ValueError("Tipo inválido. Use 'highlights' ou 'commentary'.")

    # --------------------------------
    # 1️⃣ Download do vídeo
    # --------------------------------
    print("\n📥 Baixando vídeo...")
    video_path = baixar_video(url)

    # --------------------------------
    # 2️⃣ Corte base do vídeo
    # (por enquanto fixo, depois automatizamos)
    # --------------------------------
    print("✂️ Cortando trecho do vídeo...")
    clip = cortar_trecho(video_path, inicio=15)

    # --------------------------------
    # 3️⃣ Extração de áudio (para análise)
    # --------------------------------
    print("🔊 Extraindo áudio para análise...")
    audio_temp_path = os.path.join(PASTA_AUDIOS, "audio_temp.wav")
    clip.audio.write_audiofile(audio_temp_path, logger=None)

    # --------------------------------
    # 4️⃣ Transcrição (Whisper)
    # --------------------------------
    print("🧠 Transcrevendo áudio...")
    segmentos = transcrever_video(audio_temp_path)

    # --------------------------------
    # 5️⃣ Análise do jogo / contexto
    # --------------------------------
    print("⚽ Analisando contexto...")
    sinais = extrair_sinais(segmentos)
    contexto = interpretar_jogo(sinais)

    print(f"📊 Sinais detectados: {sinais}")
    print(f"📌 Contexto interpretado: {contexto}")

    # --------------------------------
    # 6️⃣ Geração de roteiro e narração
    # (somente para highlights)
    # --------------------------------
    narracao_path = None

    if video_tipo == "highlights":
        print("✍️ Gerando roteiro automático...")
        roteiro = gerar_roteiro(contexto)

        print("🎙️ Gerando narração IA...")
        narracao_path = gerar_narracao(roteiro)

    # --------------------------------
    # 7️⃣ Aplicação das regras de áudio
    # --------------------------------
    print("🔊 Aplicando regras de áudio...")
    clip_processado, audio_tracks = aplicar_regras_audio(
        clip=clip,
        video_tipo=video_tipo,
        narracao_path=narracao_path,
        musica_path=MUSICA_PADRAO if video_tipo == "highlights" else None
    )

    # --------------------------------
    # 8️⃣ Renderização final do vídeo
    # --------------------------------
    print("🎬 Renderizando vídeo final...")
    output_path = os.path.join(PASTA_SHORTS, "short_cruzeiro.mp4")

    criar_short(
        clip=clip_processado,
        output_path=output_path,
        audio_tracks=audio_tracks,
        titulo="Cruzeiro hoje ⚽"
    )

    print("\n✅ Vídeo gerado com sucesso!")
    print(f"📂 Arquivo final: {output_path}")
