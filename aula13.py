import customtkinter as ctk
from PIL import Image #import para colocar imagem no botão

#Aqui estamos carregando a imagem para por no botão
img = ctk.CTkImage(light_image=Image.open("./envelope.png"), #se o tema for light
                   dark_image=Image.open("./envelope.png"), #se o tema for dark
                   size=(80,80)) 

# Configurando a janela principal
janela = ctk.CTk()
janela._set_appearance_mode("dark")
janela.geometry("900x700")
janela.maxsize(width=1920, height=1080)
janela.minsize(width=800, height=600)
janela.resizable(width=True, height=True)

label = ctk.CTkLabel(
    janela, text="Curso de CustomTkinter - Aula - 13", font=("arial bold", 20))
label.pack(pady=20, padx=5)





janela.mainloop()
