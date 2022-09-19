from datetime import datetime, date
cod = 0
nasc = 0
entrada = 0
cod = int(input("Qual o código do funcionário? "))
nasc = str(input("Qual a data de nascimento do funcionário? "))
entrada = str(input("Quando entrou o funcionário? "))
print("-="*30)  
print("Nascido em:",nasc)
nasc = datetime.strptime(nasc, "%d/%m/%Y").date()
entrada = datetime.strptime(entrada, "%d/%m/%Y").date()  
hoje = date.today()
idade = hoje.year - nasc.year - ((hoje.month,hoje.day) < (nasc.month,nasc.day))
tempo_trabalhado = hoje.year - entrada.year - ((hoje.month,hoje.day) < (entrada.month,entrada.day))
print(f"Idade de {idade} anos.")
print(f"O funcionário trabalha há {tempo_trabalhado} anos.")

if idade >= 60 and tempo_trabalhado >= 25:
    print("\033[31mNecessário Aposentadoria!")
elif idade >= 65 or tempo_trabalhado >= 30:
    print("\033[31mNecessário Aposentadoria!")
else:
    print("\033[32mNão necessita Aaposentadoria!")