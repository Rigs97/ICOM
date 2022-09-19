nomes = []
ver_nome = []

for n in range(0,5):
    nomes.append(str(input("Qual nome deseja informar? ")))
ver_nome.append(str(input("Qual nome deseja verificar? ")))
print("-="*30)

print(nomes)
print(ver_nome)


if ver_nome in nomes:
        print(f"O nome {ver_nome} está na lista!")
else:
    print(f"O nome {ver_nome} não está na lista!")