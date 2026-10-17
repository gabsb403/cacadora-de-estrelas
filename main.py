import tkinter as tk
import random


janela = tk.Tk()
janela.title("Caçadora de Estrelas")
janela.geometry("800x600")
janela.resizable(False, False)
janela.configure(bg="#0f112d")

tela = tk.Canvas(
    janela,
    width=800,
    height=600,
    bg="#0f112d",
    highlightthickness=0
)
tela.pack()


for i in range(100):
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    tamanho = random.randint(1, 3)

    tela.create_oval(
        x, y, x + tamanho,
        y + tamanho,
        fill="white", outline=""
)

tela.create_text(
    400, 50,
    text="Caçadora de Estrelas",
    fill="#8be9fd",
    font=("Arial", 20, "bold")
)

tela.create_polygon(
    400,250,
    375,300,
    400,290,
    425,300,
    fill="#8be9fd",
    outline="White"
)

tela.create_text(
    400, 350,
    text="Prepare-se para explorar o espaço e coletar estrelas!",
    fill="white",
    font=("Arial", 13)
)

janela.mainloop()