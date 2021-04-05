NUMERO_DE_PRODUCAO = 96
NUMERO_DE_REPETICOES = 1000
ocorrencia = {"baixa": 25 / 100, "media": 70 / 100, "alta": 100 / 100}
VARIACAO_DE_DEMANDA = {
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
CUSTO_PRODUCAO_UNITARIA = -0.25  # R$
PRECO_DE_VENDA = 0.40  # R$
PRECO_DE_VENDA_PROMOCAO = 0.30  # R$