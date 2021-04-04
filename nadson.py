import random

producao = 36
numero_de_repeticoes = 1000
ocorrencia = {"baixa": 25 / 100, "media": 70 / 100, "alta": 100 / 100}

variacao_de_demanda = {
    # TODO: Melhorar essa questão de setar as variações
    "baixa": [
        {"variacao": 0.15, "demanda": 36},
        {"variacao": 0.40, "demanda": 48},
        {"variacao": 0.75, "demanda": 60},
        {"variacao": 0.90, "demanda": 72},
        {"variacao": 0.95, "demanda": 84},
        {"variacao": 1, "demanda": 96},
    ],
}

sorteio_de_ocorrencia = round(random.random(), 2)
print("sorteio_de_ocorrencia", sorteio_de_ocorrencia)

sorteio_de_variacao_de_demanda = round(random.random(), 2)
print("sorteio_de_variacao_de_demanda", sorteio_de_variacao_de_demanda)

if ocorrencia.get("baixa") >= sorteio_de_ocorrencia:
    aux_demanda = {"subtracao_variacao": None, "demanda": 0}
    for item in variacao_de_demanda.get("baixa"):
        if item.get("variacao") >= sorteio_de_variacao_de_demanda:
            subtracao_variacao = round(
                (item.get("variacao") - sorteio_de_variacao_de_demanda), 2
            )
            if aux_demanda.get("subtracao_variacao") is not None:
                if aux_demanda.get("subtracao_variacao") > subtracao_variacao:
                    aux_demanda["subtracao_variacao"] = subtracao_variacao
                    aux_demanda["demanda"] = item.get("demanda")
            else:
                aux_demanda["subtracao_variacao"] = subtracao_variacao
                aux_demanda["demanda"] = item.get("demanda")

    print(aux_demanda)
