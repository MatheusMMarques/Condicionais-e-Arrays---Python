altura = float(input("digite sua altura: "))
peso = float(input("digite seu peso: "))

imc = peso / (altura*altura)

if (imc < 18.6):
    print("Você está abaixo do peso ideal.")
elif (18.6 <= imc <= 24.9):
    print("Você está no seu peso ideal")
elif(25 <= imc <= 29.9):
    print("Você esta acima do seu peso ideal.")
else:
    print("Você está obeso.")