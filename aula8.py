# importando a biblioteca o as é um apelido para tornar mais facil a chamada
import customtkinter as ctk

# Configurando a janela principal
janela = ctk.CTk()
janela._set_appearance_mode("dark")
janela.geometry("900x700")
janela.maxsize(width=1920, height=1080)
janela.minsize(width=800, height=600)
janela.resizable(width=True, height=True)


def abrir():
    dialog = ctk.CTkInputDialog(title="Caixa de dialogo", text="Digite o seu número de celular",
                                entry_border_color="blue", button_fg_color="green", fg_color="brown") #Atributos mais utilizados
    print("Numero de celular digitado: ", dialog.get_input())


# Criando caixa de dialogo
btn = ctk.CTkButton(janela, text="abrindo caixa de dialogo", command=abrir)
btn.pack()


janela.mainloop()
