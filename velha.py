menu = [
[" 1 ", "|", " 2 ", "|", " 3 "],
[" 4 ", "|", " 5 ", "|", " 6 "],
[" 7 ", "|", " 8 ", "|", " 9 "]
]
tabuleiro = [
[" ", "|", " ", "|", " "],
[" ", "|", " ", "|", " "],
[" ", "|", " ", "|", " "]
]
print("\n  ̊ʚ  ̊₊ ₊ ✧ᗢ ﾟ。JOGO DA VELHA  ̊ʚ  ̊₊ ₊ ✧ᗢ ﾟ。\n\nSeja bem-vindo ao nosso jogo da
velha!")
nomeO = input("\nDigite o nome do primeiro jogador: ")
nomeX = input("Digite o nome do segundo jogador: ")
# imprime o menu
print("\n")
for linha in range(3):
print("".join(menu[linha]))
if linha < 2:
print("——— ——— ———")
jogadaO = int(input(f"\n{nomeO} escolha a posição desejada: "))
jogadaX = int(input(f"{nomeX} escolha a posição desejada: "))
while (jogadaO != 1 and jogadaO != 2 and jogadaO != 3 and jogadaO != 4 and
jogadaO != 5 and jogadaO != 6 and jogadaO != 7 and jogadaO != 8 and jogadaO != 9)
or (jogadaX != 1 and jogadaX != 2 and jogadaX != 3 and jogadaX != 4 and jogadaX !=
5 and jogadaX != 6 and jogadaX != 7 and jogadaX != 8 and jogadaX != 9):
print("\nOpção inválida! Tente novamente com uma das posições indicadas abaixo:
")
print("\n")
for linha in range(3):
print("".join(menu[linha]))
if linha < 2:
print("——— ——— ———")
jogadaO = int(input(f"\n{nomeO} escolha a posição desejada: "))
jogadaX = int(input(f"{nomeX} escolha a posição desejada: "))
for i in range(3):
# jogada bolinha
if jogadaO == i + 1:
tabuleiro[0][i * 2] = " O "
menu[0][i * 2] = " "
elif jogadaO == i + 4:
tabuleiro[1][i * 2] = " O "
menu[1][i * 2] = " "
elif jogadaO == i + 7:
tabuleiro[2][i * 2] = " O "
menu[2][i * 2] = " "
# jogada xis
if jogadaX == i + 1:
tabuleiro[0][i * 2] = " X "
menu[0][i * 2] = " "
elif jogadaX == i + 4:
tabuleiro[1][i * 2] = " X "
menu[1][i * 2] = " "
elif jogadaX == i + 7:
tabuleiro[2][i * 2] = " X "
menu[2][i * 2] = " "
# imprime o tabuleiro atualizado
print("\n")
for linha in range(3):
print("".join(tabuleiro[linha]))
if linha < 2:
print("——— ——— ———")
# INÍCIO DO JOGO REPETE
ganha = 0
ganhador = "bla bla"
while ganha != 1:
print("\n")
for linha in range(3):
print("".join(menu[linha]))
if linha < 2:
print("——— ——— ———")
jogadaO = int(input(f"\n{nomeO} escolha a posição desejada: "))
jogadaX = int(input(f"{nomeX} escolha a posição desejada: "))
# opção inválida
while (jogadaO != 1 and jogadaO != 2 and jogadaO != 3 and jogadaO != 4 and
jogadaO != 5 and jogadaO != 6 and jogadaO != 7 and jogadaO != 8 and jogadaO != 9)
or (jogadaX != 1 and jogadaX != 2 and jogadaX != 3 and jogadaX != 4 and jogadaX !=
5 and jogadaX != 6 and jogadaX != 7 and jogadaX != 8 and jogadaX != 9):
print("\nOpção inválida! Tente novamente com uma das posições indicadas
abaixo: ")
print("\n")
for linha in range(3):
print("".join(menu[linha]))
if linha < 2:
print("——— ——— ———")
jogadaO = int(input(f"\n{nomeO} escolha a posição desejada: "))
jogadaX = int(input(f"{nomeX} escolha a posição desejada: "))
for i in range(3):
# jogada bolinha
if jogadaO == i + 1:
tabuleiro[0][i * 2] = " O "
menu[0][i * 2] = " "
elif jogadaO == i + 4:
tabuleiro[1][i * 2] = " O "
menu[1][i * 2] = " "
elif jogadaO == i + 7:
tabuleiro[2][i * 2] = " O "
menu[2][i * 2] = " "
# jogada xis
if jogadaX == i + 1:
tabuleiro[0][i * 2] = " X "
menu[0][i * 2] = " "
elif jogadaX == i + 4:
tabuleiro[1][i * 2] = " X "
menu[1][i * 2] = " "
elif jogadaX == i + 7:
tabuleiro[2][i * 2] = " X "
menu[2][i * 2] = " "
# imprime o tabuleiro atualizado
print("\n")
for linha in range(3):
print("".join(tabuleiro[linha]))
if linha < 2:
print("——— ——— ———")
# vencer por linha
for linha in range(3):
if tabuleiro[linha][0] == tabuleiro[linha][2] and tabuleiro[linha][2] ==
tabuleiro[linha][4] and tabuleiro[linha][0] != " ":
ganha = 1
if tabuleiro[linha][0] == " O ":
ganhador = nomeO
elif tabuleiro[linha][0] == " X ":
ganhador = nomeX
# vencer por coluna
for coluna in range(3):
if tabuleiro[0][coluna * 2] == tabuleiro[1][coluna * 2] and tabuleiro[1]
[coluna * 2] == tabuleiro[2][coluna * 2] and tabuleiro[0][coluna * 2] != " ":
ganha = 1
if tabuleiro[0][coluna * 2] == " O ":
ganhador = nomeO
elif tabuleiro[0][coluna * 2] == " X ":
ganhador = nomeX
# vencer por diagonal
if tabuleiro[0][0] == tabuleiro[1][2] and tabuleiro[1][2] == tabuleiro[2][4]
and tabuleiro[0][0] != " ":
ganha = 1
if tabuleiro[0][0] == " O ":
ganhador = nomeO
elif tabuleiro[0][0] == " X ":
ganhador = nomeX
elif tabuleiro[2][0] == tabuleiro[1][2] and tabuleiro[1][2] == tabuleiro[0][4]
and tabuleiro[0][4] != " ":
ganha = 1
if tabuleiro[2][0] == " O ":
ganhador = nomeO
elif tabuleiro[2][0] == " X ":
ganhador = nomeX
print(f"\n\n  ̊ʚ  ̊₊ ₊ ✧ᗢ ﾟ。FIM DE JOGO  ̊ʚ  ̊₊ ₊ ✧ᗢ ﾟ。\n\n{ganhador} ganhou!!!!!!!!")
