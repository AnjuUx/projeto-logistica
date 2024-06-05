
from datetime import date

hoje = date.today()



def regitre ():
 nome = (" Digite seu nome :", [nome] )
 usuario = input ("Nome de usuário :" )
 senha1 = ("Digite sua senha : " )
 senha2 = ("Digite novamente :" )

 if senha1 !=senha2 :
  print(" Senhas não compativeis ")
  return False
 return True

resultado = regitre ()
if resultado:
 print("Usuário registrado com sucesso!")
else:
 print ("Falha ao registrar usuário.")







def reg_funcionario():
 
 nome_func = input ("Nome do funcionario : " )
 matricula = int(input("Digite a matricula : " ))
 motivo = ["Quebra de caminhão", "Falta de mercadoria", "outros"]
 if motivo =="Quebra de caminhão":
  placa = input("digite a placa", )
  num_frota = input ("digite o número da frota " ) 
  caminhao = placa ,num_frota 
  
  input ("Placa ou número da frota : " )
 elif motivo == "Falta de mercadoria":
  cod_prod = int(input("Código do produto : "))
  descricao_merc = print(f'{cod_prod}', input ("Descreva o motivo : "))
 elif motivo =="outros":
  reg_funcionario()
  


 

