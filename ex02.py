k = 0
i = 2
fibonacci = [0, 1]

valorEscolhido = int(input("Digite um número inteiro a sua escolha: "))

while k == 0:

    soma = fibonacci[i-2] + fibonacci[i-1]
    fibonacci.append(soma)

    if fibonacci[i] == valorEscolhido:
        print("O número informado pertence a sequência de Fibonacci!")
        k = 1

    elif fibonacci[i] > valorEscolhido:
        print("O número informado não pertence a sequência de Fibonacci!")
        k = 1

    else:
        i += 1