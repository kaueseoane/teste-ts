palavra = input("Insira uma string: ")
palavraPrint = ""

for i in range(len(palavra), 0, -1):
    palavraPrint += palavra[i - 1]
print(palavraPrint)