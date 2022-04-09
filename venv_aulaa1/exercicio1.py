#finalizado
def exercicio1():

    valor_reais = float(input('Digite o valor em reais: '))
    cotacao_dolar  = float(input('Digite a cotação do dolar'))
    valor_dolar = cotacao_dolar * valor_reais

    print(f'O valor em dólar eh: {valor_dolar}')
    
#exercicio1()

#finalizar


def exercicio2():
  nome_produto = input('Informe o nome do produto: ') 
  quantidade_comprada = int(input('Digite a quantidade comprada: '))
  valor_unitario = float(input('Digite o valor unitario: '))
  percentual_desconto = float(input('digite o percentual de desconto'))
  percentual_desconto = (percentual_desconto * valor_unitario) / 100
  resultado = quantidade_comprada * (valor_unitario - (valor_unitario * percentual_desconto))
  print(f'nome do produto {nome_produto} valor final: {resultado}')
#exercicio2()   

#finalizado
#exercicio4
def exercicio4():
    lista_palavras = []
    for i in range (5):
        palavra = input('Digite Uma palavra:')
        lista_palavras.append(palavra)
    palavra6 = input('Digite outra palavra:')
    if (palavra6 in lista_palavras):
        print(f"A string {palavra6} está no dicionário")
    else:
        print(f"A palavra {palavra6} não está no dicionário")
#exercicio4()

#finalizado
#exercicio5
def exercicio5():
    lista_idade = []
    lista_altura = []
    tupla_idade = (lista_idade)
    tupla_altura = (lista_altura)
    
    for i in range (5):
        idade = int(input('Digite sua idade: '))
        lista_idade.append(idade)
        altura = float(input('Digite sua altura: '))
        lista_altura.append(altura)
        tupla_idade[:-1]    
    
    
    tupla_idade_invertida = list(reversed(tupla_idade))
    tupla_altura_invertida = list(reversed(tupla_altura))
    print(tupla_idade_invertida)
    print(tupla_altura_invertida)
#exercicio5()  

  