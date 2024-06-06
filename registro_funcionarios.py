import datetime



def reg_funcionario():
 
 nome_func = input ("Nome do funcionario : " )
 matricula = int(input("Digite a matricula : " ))
 dic_fucionario=[{nome_func : matricula}]
 print(dic_fucionario)
 
 
reg_funcionario()


class Ocorrencia:
  def __init__(self, data, tipo, descricao, funcionario):
    self.data = data
    self.tipo = tipo
    self.descricao = descricao
    self.funcionario = funcionario

class HistoricoOcorrencias:
  def __init__(self):
    self.ocorrencias = []



def adicionar_ocorrencia():
  data = input("Digite a data da ocorrência (YYYY-MM-DD): ")
  tipo = input("Digite o tipo de ocorrência: ")
  descricao = input("Digite a descrição da ocorrência: ")
  funcionario = input("Digite o nome do funcionário envolvido: ")

  nova_ocorrencia = Ocorrencia(datetime.datetime.strptime(data, "%Y-%m-%d"), tipo, descricao, funcionario)
  historico.adicionar_ocorrencia(nova_ocorrencia)
  print("Ocorrência adicionada com sucesso!")

adicionar_ocorrencia()