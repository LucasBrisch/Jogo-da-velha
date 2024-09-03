from tkinter import *
import random

# Variáveis para armazenar o placar
placar_O = 0
placar_X = 0

def reiniciar_jogo():
    global tabuleiro
    tabuleiro = Tabuleiro()

# Função que será chamada quando um botão for clicado
def clique(botao):
    global placar_O, placar_X
    botao.config(text="O", state=DISABLED)
    if verificar_vencedor("O"):
        placar_O += 1
        atualizar_placar()
        print("Jogador venceu!")
        reiniciar_jogo()
        return
    
    # Movimento do computador
    while True:
        botao_aleatorio = random.choice([b for linha in tabuleiro for b in linha if b["state"] == NORMAL])
        if botao_aleatorio["text"] == "":
            botao_aleatorio.config(text="X", state=DISABLED)
            break
    
    if verificar_vencedor("X"):
        placar_X += 1
        atualizar_placar()
        print("Computador venceu!")
        reiniciar_jogo()

# Função que cria o tabuleiro
def Tabuleiro():
    botoes = []
    for i in range(3):
        linha = []
        for j in range(3):
            botao = Button(janela, text="", width=20, height=6, font=("Helvetica", 24))
            botao.config(command=lambda b=botao: clique(b))
            botao.grid(row=i, column=j)
            linha.append(botao)
        botoes.append(linha)
    return botoes

# Função para verificar se há um vencedor
def verificar_vencedor(jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if all(botao["text"] == jogador for botao in linha):
            return True
    
    # Verificar colunas
    for col in range(3):
        if all(tabuleiro[row][col]["text"] == jogador for row in range(3)):
            return True
    
    # Verificar diagonais
    if all(tabuleiro[i][i]["text"] == jogador for i in range(3)):
        return True
    if all(tabuleiro[i][2-i]["text"] == jogador for i in range(3)):
        return True
    
    return False

# Função para desabilitar todos os botões
def desabilitar_todos_botoes():
    for linha in tabuleiro:
        for botao in linha:
            botao.config(state=DISABLED)

# Função para atualizar o placar
def atualizar_placar():
    label_placar_O.config(text=f"Jogador: {placar_O}")
    label_placar_X.config(text=f"Computador: {placar_X}")

# Criação da janela principal
janela = Tk()
janela.title("Jogo da Velha")
janela.geometry("1200x700")

# Labels para exibir o placar
label_placar_O = Label(janela, text=f"Jogador: {placar_O}", font=("Helvetica", 16))
label_placar_O.grid(row=3, column=0, columnspan=3)

label_placar_X = Label(janela, text=f"Computador: {placar_X}", font=("Helvetica", 16))
label_placar_X.grid(row=4, column=0, columnspan=3)

# Variável que vai receber o tabuleiro
tabuleiro = Tabuleiro()

# Loop para que a janela fique aberta
janela.mainloop()