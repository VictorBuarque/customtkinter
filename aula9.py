# importando a biblioteca o as é um apelido para tornar mais facil a chamada
import customtkinter as ctk

# Configurando a janela principal
janela = ctk.CTk()
janela._set_appearance_mode("dark")
janela.geometry("900x700")
janela.maxsize(width=1920, height=1080)
janela.minsize(width=800, height=600)
janela.resizable(width=True, height=True)


ctk.CTkLabel(janela, text="Programa do gugu", font=(
    "arial bold", 20)).pack(padx=5, pady=20)

# Criando a função de escolha


def premioEscolhido(escolha):
    print(f"O premio escolhido foi:{escolha}")


# Criando Menu - forma 1
ctk.CTkLabel(janela, text="Escolha seu premio", font=(
    "arial bold", 14)).pack(padx=5, pady=20)
premios = ctk.CTkOptionMenu(janela,  values=[
                            "Playstation", "Jogo da Vida", "Max Steel", "Bola de Futebol", "Combo do MC Donalds"],
                            command=premioEscolhido)
premios.pack(pady=10)
premios.set("Selecione um premio")

# Criando Menu - forma 2 - Atribuindo uma variavel
premio_var = ctk.StringVar(value="SELECIONAR PREMIO")
ctk.CTkLabel(janela, text="Escolha seu premio", font=(
    "arial bold", 14)).pack(padx=5, pady=20)
premios = ctk.CTkOptionMenu(janela,  values=[
                            "Playstation", "Jogo da Vida", "Max Steel", "Bola de Futebol", "Combo do MC Donalds"],
                            command=premioEscolhido, variable=premio_var, width=300, height=100,
                            bg_color="transparent", fg_color="red", corner_radius=20, text_color="black",
                            button_color="gray", button_hover_color="brown",
                            dropdown_fg_color="orange", dropdown_hover_color="yellow",
                            dropdown_text_color="black", dropdown_font=("arial", 20))  # atributos mais utilizados
premios.pack(pady=10)


janela.mainloop()
