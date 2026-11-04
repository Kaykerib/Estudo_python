print(f'\033[36m Mercadinho da esquina \033[m')
print('==================================== ' )

valor_valido = False
max_tentativas = 3

while not valor_valido:
 valor = int(input('Valor da compra: '))
 ##print(f"DEBUG:  {valor}  {type(valor)}") em qual varivel estar  o erro
 if valor > 0 and valor < 1001:
  #print(f"DEBUG:  {valor}  é entre 1 e 1000")
  valor_valido = True
 else:
  print("O valor de compra tem de ser entre 1 e 1000.")
  print('==================================== ' )
  max_tentativas=max_tentativas - 1
  if max_tentativas < 1:
   print("Alcançou o nro máximo de tentativas!")
   exit()

print('Como pretende paga as tuas compras? ' )
print('==================================== ' )
print('Dinheiro ou cheque desconto de 10% - opção 1 ')
print('==================================== ' )
print('Cartao 5% desconto - opção 2')
print('==================================== ' )
print('2x no cartão sem juros - opção 3')
print('==================================== ' )
print('3x ou mais no cartão 20% de juros - opcão 4')
print('==================================== ' )
metodo_pagamento = int((input('Qual escolha a opção: ')))

match metodo_pagamento:
    case 1:
     desc = valor * 0.10 
     total = valor - desc

    case 2:
     desc = valor * 0.05 
     total = valor - desc
    case 3:
     total = valor / 2 
 #print(f' Sua compra vai ser dividida por {total} ira paga durante 2 meses, todo dia 10')
    case 4:
     juros = valor * 0.20
     total = juros + valor
     #print(f'Com o juros a tua compra foi de {valor} para {total} com o 20% de juros ')
    case _:
     print('Não tem esta opção acima')


print(f'O valor total a paga pela tua compra ficou em {total}')