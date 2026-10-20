lista = ['Ana', 'Pedro', 'Carlos']
print(f"A lista atual de convidados é {lista}")
nome = input("Digite o nome do novo convidado: ")
posicao = int(input("Digite a posição na qual quer inserir o convidado: "))
lista.insert(posicao - 1,nome)
print(lista)