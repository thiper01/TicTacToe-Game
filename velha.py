def initialize():
    M = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(".")
        M.append(linha)
    return M

def imprime(M):
    for i in range(3):
        for j in range(3):
            print(M[i][j], end=" ")
        print()
    
def step(M, lin, col, gamer):
    if M[lin][col] == ".":
        M[lin][col] = gamer
        return M, True
    else:
        return M, False

def status(M):
    #verificando se jogador X ganhou na linha
    for i in range(3):
        countX = 0
        countO = 0
        for j in range(3):
            if M[i][j] == "X":
                countX+=1
            if M[i][j] == "0":
                countO+=1
        if countX == 3 or countO ==3:
            return True

    #verificando se jogador X ganhou na coluna
    for i in range(3):
        countX = 0
        countO = 0
        for j in range(3):
            if M[j][i] == "X":
                countX+=1
            if M[j][i] == "0":
                countO+=1
        if countX == 3 or countO ==3:
            return True

    #verificando se jogador X ganhou na diagonal principal
    countX = 0
    countO = 0
    for i in range(3):        
        if M[i][i] == "X":
            countX+=1
        if M[i][i] == "0":
            countO+=1
    if countX == 3 or countO ==3:
        return True

    #verificando se jogador X ganhou na diagonal secundária
    countX = 0
    countO = 0
    for i in range(3, -1):
        if M[i][2-i] == "X":
            countX+=1
        if M[i][2-i] == "0":
            countO+=1
    if countX == 3 or countO ==3:
        return True

    #se ninguém venceu
    return False
            

def main():
    print(" ------- Jogo da velha ---------")
    M = initialize()
    imprime(M)
    for i in range(9):
        if i%2 == 0:
            print(" Jogador 1 ('X'): ")
            verifica = False
            while verifica == False:
                lin = int(input(" Digite a linha: "))-1
                col = int(input(" Digite a coluna: "))-1
                M, verifica = step(M, lin, col, "X")
                if verifica == False:
                    print("Posição já ocupada")
            print("\n\n")
            imprime(M)
            if status(M) == True:
                print("Jogador 1 você venceu!")
                break
        else:
            print(" Jogador 2 ('0'): ")
            verifica = False
            while verifica == False:
                lin = int(input(" Digite a linha: "))-1
                col = int(input(" Digite a coluna: "))-1
                M, verifica = step(M, lin, col, "0")
                if verifica == False:
                    print("Posição já ocupada")
            print("\n\n")
            imprime(M)
            if status(M) == True:
                print("Jogador 2 você venceu!")
                break
        print("\n\n")

    if i == 9:
        print("Ninguém venceu!")

    print("Game Over!")


main()
