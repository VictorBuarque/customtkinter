# importando a biblioteca o as é um apelido para tornar mais facil a chamada
import customtkinter as ctk

# Configurando a janela principal
janela = ctk.CTk()
janela._set_appearance_mode("dark")
janela.geometry("900x700")
janela.maxsize(width=1920, height=1080)
janela.minsize(width=800, height=600)
janela.resizable(width=True, height=True)

# Criação de caixa de texto = TextBox
textbox = ctk.CTkTextbox(janela, width=300, height=350, scrollbar_button_color="green",
                         scrollbar_button_hover_color="lightgreen", border_color="yellow", border_width=5, 
                         border_spacing=20, corner_radius=15, fg_color="teal", text_color="white", 
                         activate_scrollbars="True") #Atributos mais utilizados
textbox.pack()
# Texto dentro da caixa, bom para help.
textbox.insert("0.0", "Titulo do texto\n\n" +
               "Olá muchachos! Segura a cabeça de mamãe\n\n"*20)


janela.mainloop()
