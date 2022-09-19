tm = int(input("Qual o total de mercadorias em estoque? "))
total = list()
nome = list()
valor = list()

for c in range (0,tm):
    nome.append(str(input("Qual o nome da mercadoria? ")))
    valor.append(int(input("Qual o valor da mercadoria? ")))
    total.append(valor[:])
print("O valor total das mercadorias é:",sum(valor))
print("A média dos valores da mercadoria é de:",sum(valor)/len(valor))