despensa = ["Arroz", "Salgadinho", "Leite Condensado"]
item_desejado = input("Qual o item que você deseja verificar? ")
if item_desejado in despensa:
    print(f"O item {item_desejado} está na despensa")
else:
    print(f"O item {item_desejado} não se encontra na despensa")
