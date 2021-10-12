import json

f = open("ex03.json")
data = json.load(f)

def menor_valor():
    menorValor = 9999999999999999.0
    valorInicial = float

    for i in data["mes"]:
            if i["valor"] != 0:
                valorInicial = float(i["valor"])
                if valorInicial <= menorValor:
                    menorValor = valorInicial
    print("O menor faturamento em um dia foi de R$", menorValor, ".")

def maior_valor():
    maiorValor = 0.0
    valorInicial = float

    for i in data["mes"]:
            if i["valor"] != 0:
                valorInicial = float(i["valor"])
                if valorInicial >= maiorValor:
                    maiorValor = valorInicial
    print("O maior faturamento em um dia foi de R$", maiorValor, ".")

def media_mensal():
    soma = 0.0
    k = 0
    dias = 0

    for i in data["mes"]:
            if i["valor"] != 0:
                soma += float(i["valor"])
                k += 1
    media = soma/k
    for i in data["mes"]:
            if i["valor"] > media:
                dias += 1
    print("Em", dias, "dias o valor de faturamento diário foi superior à média mensal.")

menor_valor()
maior_valor()
media_mensal()