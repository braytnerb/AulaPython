'''def gerar_tabuada (numero):
        print(f"A tabuada de soma de {numero}:")
        for i in range (1,11):
            resultado = numero + i
            print(f"{numero}  + {i} =  {resultado}")

            

numero = int(input("Digite o numero: "))
if 1 <= numero <= 10:
    gerar_tabuada(numero)
else:
    print("Numero fora do intervalo!!")'''


acumulador = 0
voltas = 0


while True:
    nota = float(input("Digite a nota: "))
    if nota == -1: 
        break
    acumulador += nota
    voltas +=1

media = acumulador/voltas

print(f"{media}")
