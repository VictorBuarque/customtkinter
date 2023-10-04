# importando a biblioteca o as é um apelido para tornar mais facil a chamada
import customtkinter as ctk
# Criando nova janela


def nova_tela():
    # exemplo de utilização tela de login
    nova_janela = ctk.CTkToplevel(janela, fg_color="teal")
    nova_janela.geometry = ("200x200")


# Configurando a janela principal
janela = ctk.CTk()  # criar janela
janela.title("Custom Tkinter")  # Titulo do programa
# tema da tela (pode ser #dark, #light ou #system)
janela._set_appearance_mode("dark")
janela.geometry("900x700")  # tamanho inicial da tela
janela.maxsize(width=1920, height=1080)  # tamanho máximo da tela
janela.minsize(width=800, height=600)  # tamanho minimo da tela
# Habilitar redimensinonamento da tela
janela.resizable(width=True, height=True)
# janela.iconify() #fechar janela
# janela.deiconify() #abrir janela se não abriu a janela antes não funciona

# Criando Frames
# (bg_color = background_color, fg_color = foreground_color, border_widht = tamanho da borda, corner_radius = border_radius)
frame1 = ctk.CTkFrame(janela, width=200, height=330, fg_color="blue", bg_color="transparent", border_width=10,
                      border_color="red", corner_radius=30).place(x=10, y=60)
frame2 = ctk.CTkFrame(janela, width=200, height=330,
                      fg_color="yellow").place(x=230, y=60)
frame2 = ctk.CTkFrame(janela, width=200, height=330,
                      fg_color="teal").place(x=450, y=60)


btn_novatela = ctk.CTkButton(
    master=janela, text="Abrir nova janela", command=nova_tela).place(x=300, y=100)


janela.mainloop() #Iniciar o programa
