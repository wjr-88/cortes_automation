def gerar_roteiro(contexto):
    if contexto == "vitória sofrida":
        return (
            "O Cruzeiro venceu, mas não convenceu.\n"
            "O time sofreu pressão, brigou até o fim,\n"
            "e a torcida saiu aliviada.\n"
            "Vitória importante, mas o sinal de alerta segue ligado."
        )

    if contexto == "vitória controlada":
        return (
            "O Cruzeiro mostrou controle e eficiência.\n"
            "Criou chances, marcou gols\n"
            "e confirmou o resultado.\n"
            "Será o início de uma reação?"
        )

    if contexto == "pressão sem resultado":
        return (
            "O Cruzeiro tentou, pressionou,\n"
            "mas a vitória não veio.\n"
            "A torcida cobra,\n"
            "e o momento segue delicado."
        )

    return (
        "Jogo equilibrado do Cruzeiro.\n"
        "Muita disputa, poucas chances claras,\n"
        "e um resultado que reflete o que foi o jogo."
    )
