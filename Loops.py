# Seleteção de Exercícios em Python

exercicio = input("Selecione o exercício (1-3): ")

match exercicio:

#exercicio 1

    case "1":

        print("Exercício 1: Tabuada")
        numero = int(input("Digite um número para ver a tabuada: "))
        for i in range(1, 11):
            print (f"{numero} x {i} = {numero * i}")

#exercicio 2

    case "2":

        print("Exercício 2: Soma Primos")

        for i in range(1, 101,2):
            i += i
        print(i)

#exercicio 3

    case "3":

        print("Exercício 3: Frase Repetir")

        while True:
            frase = input("Digite uma frase (ou 'sair' para encerrar): ")
            if frase.lower() == 'sair':
                break
            print(f"Você digitou: {frase}")