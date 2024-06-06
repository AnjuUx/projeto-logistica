


def regitre (registro):
 nome = input(" Digite seu nome : " )
 usuario = input ("Nome de usuário :" )
 senha1 = input("Digite sua senha : " )
 senha2 = input("Digite novamente : " )

 if senha1 !=senha2 :
  print(" Senhas não compativeis ")
  return False
 return True

resultado = regitre ()
if resultado:
 print("Usuário registrado com sucesso!")
else:
 print ("Falha ao registrar usuário.")


