# importando a biblioteca o as é um apelido para tornar mais facil a chamada
import customtkinter as ctk

# Configurando a janela principal
janela = ctk.CTk()
janela._set_appearance_mode("dark")
janela.geometry("900x700")
janela.maxsize(width=1920, height=1080)
janela.minsize(width=800, height=600)
janela.resizable(width=True, height=True)

label = ctk.CTkLabel(
    janela, text="Curso de CustomTkinter - Aula - 10", font=("arial bold", 20))
label.pack(pady=20, padx=5)

label2 = ctk.CTkLabel(janela, text="Digite o seu nome completo.").pack()

# Trabalhando com label de forma dinamica
# 1 - forma introduzindo o texto por input
# Não é prático porque o usuário não vai utilizar o terminal.
text_var = ctk.StringVar(value=input("Digite seu nome completo: "))
lab = ctk.CTkLabel(janela, textvariable=text_var, width=200,
                   height=25, text_color="blue", font=("verdana bold", 16))
lab.pack(pady=10)

# 2 - Introduzindo o texto por entry (forma mais prática)

def enviar_texto():
    t = entry.get()
    lab2.configure(text=str(t))


lab2 = ctk.CTkLabel(janela, text="", width=200, height=25,
                    text_color="blue", font=("verdana bold", 16))
lab2.pack(pady=10)
entry = ctk.CTkEntry(janela, width=200)
entry.pack()  #o entry o pack tem que escrever assim se não não funciona o get

botao = ctk.CTkButton(janela, text="enviar", width=200,
                      command=enviar_texto).pack()


janela.mainloop()
