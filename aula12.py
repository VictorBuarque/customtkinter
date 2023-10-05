import customtkinter as ctk
from PIL import Image #import para colocar imagem no botão

#Aqui estamos carregando a imagem para por no botão
img = ctk.CTkImage(light_image=Image.open("./envelope.png"), dark_image=Image.open("./envelope.png"), size=(80,80)) 

# Configurando a janela principal
janela = ctk.CTk()
janela._set_appearance_mode("dark")
janela.geometry("900x700")
janela.maxsize(width=1920, height=1080)
janela.minsize(width=800, height=600)
janela.resizable(width=True, height=True)

label = ctk.CTkLabel(
    janela, text="Curso de CustomTkinter - Aula - 12", font=("arial bold", 20))
label.pack(pady=20, padx=5)

ctk.CTkButton(janela, text="click", width=300, height=300, 
              fg_color="transparent",bg_color="teal", 
              hover_color="white", corner_radius=20,
              text_color="red", font=("arial",20),
              border_color="blue", border_spacing=5, 
              border_width=3, state="normal",
              image=img).pack(pady=20) 
#Atributos mais utilizados para botões, para renderizar a imagem tem que atribuir a variável image=img

janela.mainloop()
