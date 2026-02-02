# main.py

import os

from utils.downloader import baixar_video
from utils.transcriber import transcrever_audio
from utils.game_analysis import analisar_contexto, interpretar_jogo
from utils.script_generator import gerar_roteiro
from utils.cutter import cortar_trecho
from utils.video import (
    remover_audio,
    adicionar_musica_fundo,
    manter_audio_original
)

# =========================
# CONFIGURAÇÕES BÁSICAS
# =========================
PASTA_VIDEOS = "videos"
PASTA_OUTPUT = "output"
PASTA_ROTEIROS = "roteiros"
MUSICA_FUNDO = "assets/musica_fundo.mp3"  # ajuste depois


# =========================
# PIPELINE PRINCIPAL
# =========================
def processar_video(url, tipo_video):
    """
    Pipeline principal de processamento do vídeo
    """

    os.makedirs(PASTA_VIDEOS, exist_ok=True)
    os.makedirs(PASTA_OUTPUT, exist_ok=True)
    os.makedirs(PASTA_ROTEIROS, exist_ok=True)

    print("\n📥 Baixando vídeo...")
    video_path = baixar_video(url, PASTA_VIDEOS)

    print("🎧 Transcrevendo áudio...")
    transcricao = transcrever_audio(video_path)

    segmentos = transcricao["segments"]

    print("🧠 Analisando contexto do jogo...")
    sinais = analisar_contexto(segmentos)
    contexto_jogo = interpretar_jogo(sinais)

    print(f"📊 Contexto detectado: {contexto_jogo}")

    print("✍️ Gerando roteiro automático...")
    roteiro = gerar_roteiro(contexto_jogo, tipo_video)

    nome_base = os.path.splitext(os.path.basename(video_path))[0]

    roteiro_path = os.path.join(PASTA_ROTEIROS, f"{nome_base}.txt")
    with open(roteiro_path, "w", encoding="utf-8") as f:
        f.write(roteiro)

    print(f"📝 Roteiro salvo em: {roteiro_path}")

    print("✂️ Gerando corte para Short...")
    short_path = cortar_trecho(
        video_path=video_path,
        inicio=0,
        duracao=60,
        output_dir=PASTA_OUTPUT
    )

    print("🎬 Tratando áudio do vídeo...")
    if tipo_video == "melhores_momentos":
        short_sem_audio = remover_audio(short_path)
        short_final = adicionar_musica_fundo(short_sem_audio, MUSICA_FUNDO)
    else:
        short_final = manter_audio_original(short_path)

    print(f"\n✅ Vídeo final gerado com sucesso:")
    print(short_final)


# =========================
# EXECUÇÃO INTERATIVA
# =========================
if __name__ == "__main__":

    print("\n==============================")
    print("🎬 AUTOMAÇÃO DE SHORTS - CRUZEIRO")
    print("==============================\n")

    url = input("Cole o link do vídeo do YouTube: ").strip()

    print("\nTipo de vídeo:")
    print("1 - Melhores momentos (sem áudio + música)")
    print("2 - Jornalístico / Comentários (mantém áudio)")

    tipo = input("Escolha (1 ou 2): ").strip()

    if tipo == "1":
        tipo_video = "melhores_momentos"
    elif tipo == "2":
        tipo_video = "jornalismo"
    else:
        print("❌ Opção inválida. Encerrando.")
        exit(1)

    processar_video(url, tipo_video)
