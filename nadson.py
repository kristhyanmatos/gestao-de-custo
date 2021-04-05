import random
import statistics

numero_de_producao = 36
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
    "media": [
        {"variacao": 0.10, "demanda": 36},
        {"variacao": 0.30, "demanda": 48},
        {"variacao": 0.60, "demanda": 60},
        {"variacao": 0.85, "demanda": 72},
        {"variacao": 0.95, "demanda": 84},
        {"variacao": 1, "demanda": 96},
    ],
    "alta": [
        {"variacao": 0.05, "demanda": 36},
        {"variacao": 0.15, "demanda": 48},
        {"variacao": 0.40, "demanda": 60},
        {"variacao": 0.70, "demanda": 72},
        {"variacao": 0.90, "demanda": 84},
        {"variacao": 1, "demanda": 96},
    ],
}
custo_de_producao_unitaria = -0.25  # R$
preco_de_venda = 0.40  # R$
preco_de_venda_promocao = 0.30  # R$
lucros = []


def define_demanda(vetor_de_demandas, sorteio_de_variacao_de_demanda):
    aux_demanda = {"subtracao_variacao": None, "demanda": 0}
    for item in vetor_de_demandas:
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

    return aux_demanda.get("demanda")

def calcula_custos():
    for interacao in range(numero_de_repeticoes):
        saldo_venda_promocao = 0
        saldo_perda_venda = 0
        saldo_venda = 0

        sorteio_de_ocorrencia = round(random.random(), 2)
        sorteio_de_variacao_de_demanda = round(random.random(), 2)

        demanda = None
        if ocorrencia.get("baixa") >= sorteio_de_ocorrencia:
            demanda = define_demanda(
                variacao_de_demanda.get("baixa"), sorteio_de_variacao_de_demanda
            )
        elif (
            ocorrencia.get("baixa") < sorteio_de_ocorrencia
            and ocorrencia.get("media") >= sorteio_de_ocorrencia
        ):
            demanda = define_demanda(
                variacao_de_demanda.get("media"), sorteio_de_variacao_de_demanda
            )
        elif (
            ocorrencia.get("media") < sorteio_de_ocorrencia
            and ocorrencia.get("alta") >= sorteio_de_ocorrencia
        ):
            demanda = define_demanda(
                variacao_de_demanda.get("alta"), sorteio_de_variacao_de_demanda
            )

        # Cáculo de Custo de Produção $ 24
        custo_de_producao = numero_de_producao * custo_de_producao_unitaria

        # Cálculo de Verificação de rendimento 8
        resto_de_venda = numero_de_producao - demanda

        # Cálculo de venda na promoção
        if resto_de_venda > 0:
            # Cálculo de Venda
            saldo_venda = demanda * preco_de_venda
            saldo_venda_promocao = round((resto_de_venda * preco_de_venda_promocao), 2)

        elif resto_de_venda < 0:
            # Cálculo de perda de venda
            saldo_venda = numero_de_producao * preco_de_venda
            saldo_perda_venda = round(
                (resto_de_venda * (preco_de_venda + custo_de_producao_unitaria)), 2
            )
        else:
            saldo_venda = numero_de_producao * preco_de_venda
        # Cálculo de saldo total
        saldo_total = (
            saldo_venda_promocao + saldo_venda + custo_de_producao + saldo_perda_venda
        )
        lucros.append(saldo_total)
    print("soma", sum(lucros))
    print("média", statistics.mean(lucros))
    return lucros