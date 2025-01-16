# Receita do dia
receita = float(input('Receita do dia: R$'))

# KM rodado
km_rodado = float(input('Quantos KM rodados: '))

# CUSTOS #
km_por_litro = None
economia = None      # quantos reais custa cada KM

# preço do combustivel
gasolina = 6.50
etanol = 4

# Combustivel utilizado #
while True:
    combustivel = input('[G]asolina ou [E]tanol: ')[0].lower()

    if combustivel in 'g':
        combustivel = 'Gasolina'
        km_por_litro = float(input('Quantos KM seu carro faz por litro: '))
        economia = gasolina / km_por_litro
        break
    elif combustivel in 'e':
        combustivel = 'Etanol'
        km_por_litro = float(input('Quantos KM seu carro faz por litro: '))
        economia = etanol / km_por_litro
        break
    else:
        print('INVÁLIDO!\n'
              'Selecione:')

# custo com combustivel
combustivel_utilizado = km_rodado * economia

# custo com pneu e oleo
pneu = km_rodado * 0.03  # @  50k rodados levando em consideração R$1000 jogo de pneu (tirando 3 centavos por km)
oleo = km_rodado * 0.03  # @   10k rodados para troca de oleo em consideração R$250 (tirando 3 centavos por km)

# Custos gerais dos demais componentes
manutencao_geral = km_rodado * 0.20   # @  tirando 20 centavos por km rodado (pode tirar quanto quiser)

# TOTAL DOS CUSTOS
custo_total = combustivel_utilizado + pneu + oleo + manutencao_geral

# LUCRO
lucro = receita - custo_total


# Esboço de como deve aparecer o relatório
print(f'\n'
      f'{20 * '-'}\n'
      f'Relatório:\n'
      f'{20 * '-'}\n'
      f'Receita: R${receita:.2f}\n'
      f'Km rodado: {km_rodado}\n'
      f'Combustivel utilizado: {combustivel}\n'
      f'Custo com combustível: R${combustivel_utilizado:.2f}\n'
      f'Pneu: R${pneu:.2f}\n'
      f'Oleo: R${oleo:.2f}\n'
      f'Manutenção geral: R${manutencao_geral:.2f}\n'
      f'{20 * '-'}\n'
      f'CUSTO TOTAL: R${custo_total}\n'
      f'LUCRO: R${lucro:.2f}\n'
      f'{20 * '-'}')

''' 
da pra fazer tudo isso em dicionario, e deixar a opção por motorista alterar alguns dados.
por exemplo: ele alterar o quanto quer guardar pra oleo, pneu ou mecanico geral.
mas a príncipio o básico dos cálculos é isso.
deixei um    '@'    onde daria para ele alterar quando quisesse.
'''
