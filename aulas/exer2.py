while True:
    entrada = input("digite sua idade: ")
    if entrada.strip() == "":
        print("preencha o campo com algum valor")
    else:
        try:
            vIdade = int(entrada)
            break
        except ValueError:
            print("Digite um número válido.")

if vIdade < 18:
    print("Jovem")
elif vIdade >= 18 and vIdade < 60:
    print("Adulto")
else:
    print("Idoso")