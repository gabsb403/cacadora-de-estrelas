
import tkinter as tk

janela = tk.Tk()
janela.title("Teste")
janela.geometry("500x300")

tk.Label(
    janela,
    text="Minha janela está funcionando!",
    font=("Arial", 16)
).pack(pady=100)

janela.mainloop()
