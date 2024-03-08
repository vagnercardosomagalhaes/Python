
qtd = 0
while qtd < 3:
    usr = input("Digite usuario: ")
    psw = input("Digite a senha: ")       
    if psw == "teste" and usr == "vagner":
        for qtd in range(1, 7):
            print("Senha correta")
        break
    else:
        print("senha errada")
    qtd += 1

print("Fim")