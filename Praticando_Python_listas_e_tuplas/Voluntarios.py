nomes = []

while True:
    nome = input("Digite um nome do voluntario (ou 'sair' para encerrar): ")
    if nome == "sair":
        break
    nomes.append(nome)

print(nomes)