temp = list()
dias = int(input("Quantos dias deseja informar? "))

for c in range(dias):
    temp.append(int(input(f"Qual foi a temperatura reguistrada no dia {c}? ")))
    
media = sum(temp)/len(temp)
print("-="*30)
for c, v  in enumerate(temp):
    if temp[c] < media:
        print(f"A temperatura foi inferior no dia {c} ")
        
print(f"As temperaturas foram de: {temp}")
print("A maior temperatura foi:",max(temp))
print("A menor temperatura foi:",min(temp))
print("A temperatura média foi de",media)


#a) Menor temperatura 
#b) Maior temperatura 
#c) Temperatura média 
#d) O número de dias em que a temperatura foi inferior a média.