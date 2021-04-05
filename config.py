NUMERO_DE_PRODUCAO = 72
NUMERO_DE_REPETICOES = 1000
ocorrencia = {"baixa": 25 / 100, "media": 70 / 100, "alta": 100 / 100}
VARIACAO_DE_DEMANDA = {
    "baixa": [
        {"variacao": 0.15, "demanda": 72},
        {"variacao": 0.40, "demanda": 96},
        {"variacao": 0.75, "demanda": 120},
        {"variacao": 0.90, "demanda": 144},
        {"variacao": 0.95, "demanda": 168},
        {"variacao": 1, "demanda": 192},
    ],
    "media": [
        {"variacao": 0.10, "demanda": 72},
        {"variacao": 0.30, "demanda": 96},
        {"variacao": 0.60, "demanda": 120},
        {"variacao": 0.85, "demanda": 144},
        {"variacao": 0.95, "demanda": 168},
        {"variacao": 1, "demanda": 192},
    ],
    "alta": [
        {"variacao": 0.05, "demanda": 72},
        {"variacao": 0.15, "demanda": 96},
        {"variacao": 0.40, "demanda": 120},
        {"variacao": 0.70, "demanda": 144},
        {"variacao": 0.90, "demanda": 168},
        {"variacao": 1, "demanda": 192},
    ],
}
CUSTO_PRODUCAO_UNITARIA = -4.99  # R$
PRECO_DE_VENDA = 6.99  # R$
PRECO_DE_VENDA_PROMOCAO = 5.61  # R$