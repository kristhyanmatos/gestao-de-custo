import random
import statistics

lucros = []
lucros_baixa_ocorrencia = []
lucros_media_ocorrencia = []
lucros_alta_ocorrencia = []

import config


def define_demanda(vetor_de_demandas, sorteio_de_VARIACAO_DE_DEMANDA):
    aux_demanda = {"subtracao_variacao": None, "demanda": 0}
    for item in vetor_de_demandas:
        if item.get("variacao") >= sorteio_de_VARIACAO_DE_DEMANDA:
            subtracao_variacao = round(
                (item.get("variacao") - sorteio_de_VARIACAO_DE_DEMANDA), 2
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
    for interacao in range(config.NUMERO_DE_REPETICOES):
        tipo_ocorrencia = None
        saldo_venda_promocao = 0
        saldo_perda_venda = 0
        saldo_venda = 0

        sorteio_de_ocorrencia = round(random.random(), 2)
        sorteio_de_VARIACAO_DE_DEMANDA = round(random.random(), 2)

        demanda = None
        if config.ocorrencia.get("baixa") >= sorteio_de_ocorrencia:
            demanda = define_demanda(
                config.VARIACAO_DE_DEMANDA.get("baixa"), sorteio_de_VARIACAO_DE_DEMANDA
            )
            tipo_ocorrencia = "baixa"
        elif (
            config.ocorrencia.get("baixa") < sorteio_de_ocorrencia
            and config.ocorrencia.get("media") >= sorteio_de_ocorrencia
        ):
            demanda = define_demanda(
                config.VARIACAO_DE_DEMANDA.get("media"), sorteio_de_VARIACAO_DE_DEMANDA
            )
            tipo_ocorrencia = "media"
        elif (
            config.ocorrencia.get("media") < sorteio_de_ocorrencia
            and config.ocorrencia.get("alta") >= sorteio_de_ocorrencia
        ):
            demanda = define_demanda(
                config.VARIACAO_DE_DEMANDA.get("alta"), sorteio_de_VARIACAO_DE_DEMANDA
            )
            tipo_ocorrencia = "alta"

        # Cáculo de Custo de Produção
        custo_de_producao = config.NUMERO_DE_PRODUCAO * config.CUSTO_PRODUCAO_UNITARIA

        # Cálculo de Verificação de rendimento 8
        resto_de_venda = config.NUMERO_DE_PRODUCAO - demanda

        # Cálculo de venda na promoção
        if resto_de_venda > 0:
            # Cálculo de Venda
            saldo_venda = demanda * config.PRECO_DE_VENDA
            saldo_venda_promocao = round(
                (resto_de_venda * config.PRECO_DE_VENDA_PROMOCAO), 2
            )

        elif resto_de_venda < 0:
            # Cálculo de perda de venda
            saldo_venda = config.NUMERO_DE_PRODUCAO * config.PRECO_DE_VENDA
            saldo_perda_venda = round(
                (
                    resto_de_venda
                    * (config.PRECO_DE_VENDA + config.CUSTO_PRODUCAO_UNITARIA)
                ),
                2,
            )
        else:
            saldo_venda = config.NUMERO_DE_PRODUCAO * config.PRECO_DE_VENDA
        # Cálculo de saldo total
        saldo_total = (
            saldo_venda_promocao + saldo_venda + custo_de_producao + saldo_perda_venda
        )
        if tipo_ocorrencia == "baixa":
            lucros_baixa_ocorrencia.append(saldo_total)
        elif tipo_ocorrencia == "media":
            lucros_media_ocorrencia.append(saldo_total)
        elif tipo_ocorrencia == "alta":
            lucros_alta_ocorrencia.append(saldo_total)

        lucros.append(saldo_total)
    return lucros


def media_lucro():
    if len(lucros) > 0:
        return round(statistics.mean(lucros), 2)
    else:
        return 0


def media_lucro_baixa_ocorrencia():
    if len(lucros_baixa_ocorrencia) > 0:
        return round(statistics.mean(lucros_baixa_ocorrencia), 2)
    else:
        return 0


def media_lucro_media_ocorrencia():
    if len(lucros_media_ocorrencia) > 0:
        return round(statistics.mean(lucros_media_ocorrencia), 2)
    else:
        return 0


def media_lucro_alta_ocorrencia():
    if len(lucros_alta_ocorrencia) > 0:
        return round(statistics.mean(lucros_alta_ocorrencia), 2)
    else:
        return 0