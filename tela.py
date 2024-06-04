import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme ("dark-blue")

janela = customtkinter.CTk ()
janela.geometry ("500x500")

def clique():
    print("Fazer Login")

texto = customtkinter.CTkLabel(janela, text = "Fazer Login")
usuario = customtkinter.CTkEntry(janela, placeholder_text ="usuario")
senha= customtkinter.CTkEntry(janela, placeholder_text ="senha", show = "*")
botao_login= customtkinter.CTkButton(janela, text="Login",  command= clique)

texto.pack(padx=10, pady=10)
usuario.pack(padx=10, pady=10)
senha.pack(padx=10, pady=10)
botao_login.pack(padx=10, pady=10)




janela.mainloop()