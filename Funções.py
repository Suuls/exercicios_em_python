# Seleteção de Exercícios em Python

exercicio = input("Selecione o exercício (1-2): ")

match exercicio:

#exercicio 1

    case "1":

        print("Exercício 1: Fatorial")
        def fatorial(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * fatorial(n - 1)
        numero = int(input("Digite um número para calcular o fatorial: "))
        print (f"O fatorial de {numero} é {fatorial(numero)}")

#exercicio 2

    case "2":

        print("Exercício 2: Primos")

        def eh_primo(numero):
            if numero <= 1:
                return False
            for i in range (2, int((numero**0.5)) + 1):
                if numero % i == 0:
                    return False
            return True
        try:
            num_digitado = int(input("Digite um número para verificar se é primo: "))
            if eh_primo(num_digitado):
                print(f"{num_digitado} é um número primo.")
            else:
                print(f"{num_digitado} não é um número primo.")
        except ValueError:
            print("Por favor, digite um número válido.")