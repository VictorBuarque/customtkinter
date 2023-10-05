# importando a biblioteca o as é um apelido para tornar mais facil a chamada
import customtkinter as ctk
from tkinter import *

# Configurando a janela principal
janela = ctk.CTk()
janela._set_appearance_mode("dark")
janela.geometry("900x700")
janela.maxsize(width=1920, height=1080)
janela.minsize(width=800, height=600)
janela.resizable(width=True, height=True)
label = ctk.CTkLabel(
    janela, text="Curso de CustomTkinter - Aula - 11", font=("arial bold", 20))
label.pack(pady=20, padx=5)

def salvar():
    t = entry.get()
    print(t)  # sempre printar pra saber se está funcionando
    entry.delete(0, END)  # Limpa o campo do entry
    pass

"""def apagar():
    t= entry.delete(0,END) #A função END só funciona juntamente com o import do TKINTER original
    pass"""

# Criando Entrys
entry = ctk.CTkEntry(janela, width=200,
                     placeholder_text="Digite o seu nome:",
                     placeholder_text_color="green",
                     fg_color="white",
                     text_color="Orange",
                     border_color="lightblue",
                     border_width=20,
                     font=("Arial bold", 20),
                     corner_radius=20,
                     state="normal")  # O atributo state é o que vai habilitar ou desabilitar o entry (normal ou disable)
entry.pack(pady=20)

ctk.CTkButton(janela, width=200, text="Salvar", command=salvar).pack(pady=5)
# ctk.CTkButton(janela, width=200, text="Apagar", command=apagar).pack(pady=5)

janela.mainloop()
