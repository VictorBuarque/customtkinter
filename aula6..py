# importando a biblioteca o as é um apelido para tornar mais facil a chamada
import customtkinter as ctk

# Configurando a janela principal
janela = ctk.CTk()
janela._set_appearance_mode("dark")
janela.geometry("900x700")
janela.maxsize(width=1920, height=1080)
janela.minsize(width=800, height=600)
janela.resizable(width=True, height=True)

# Criando tabviews (Abas)
tabview = ctk.CTkTabview(janela, width=400, corner_radius=20, height=400, border_color="green", border_width=5,
                         fg_color="black",
                         segmented_button_fg_color="yellow",
                         segmented_button_selected_color="red",
                         segmented_button_selected_hover_color="blue",
                         segmented_button_unselected_hover_color="purple")  # atributos interessantes de se utilizar

# não pode colocar o pack na mesma linha de criação da variavel inicial da erro, sempre fazer assim!
tabview.pack(padx=20, pady=20)
tabview.add("Nomes")
tabview.add("Idade")
tabview.add("Genero")
tabview.add("Telefone")
tabview.tab("Nomes").grid_columnconfigure(0, weight=1)
tabview.tab("Idade").grid_columnconfigure(0, weight=1)
tabview.tab("Genero").grid_columnconfigure(0, weight=1)
tabview.tab("Telefone").grid_columnconfigure(0, weight=1)

# Adicionando elementos
text = ctk.CTkLabel(tabview.tab("Nomes"),
                    text="Victor Gabriel\n""Ana Maria\n""Carla Cristina\n")
text.pack()
idd = ctk.CTkLabel(tabview.tab("Idade"), text="31\n""22\n""21\n")
idd.pack()
gen = ctk.CTkLabel(tabview.tab("Genero"),
                   text="Masculino\n""Feminino\n""Feminino\n")
gen.pack()


janela.mainloop()
