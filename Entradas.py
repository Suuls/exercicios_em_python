# Seleteção de Exercícios em Python

exercicio = input("Selecione o exercício (1-2): ")

# Exercicio 1

match exercicio:

    # Exercicio 1

    case "1":
        numero1 = input("Digite o primeiro número: ")
        numero2 = input("Digite o segundo número: ")

        if numero1 > numero2:
            print(f"{numero1} é maior que {numero2}")
        elif numero1 < numero2:
            print(f"{numero1} é menor que {numero2}")
        else:
            print(f"{numero1} é igual a {numero2}")

# Exercicio 2

    case "2":

        while True:
            genero = input("Digite seu gênero (M/F): ").strip().upper()

            if genero in ["M", "F"]:
                if genero == "M":
                    print("Você é do gênero Masculino.")
                else:
                    print("Você é do gênero Feminino.")
                break
            else:
                print("Gênero inválido. Por favor, digite 'M' para Masculino ou 'F' para Feminino.")
        
    case _:
        print("Exercício inválido. Por favor, selecione 1 ou 2.")

