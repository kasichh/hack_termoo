import pandas as pd

bd = pd.read_csv('https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt')

tamanho = bd.Aarao.map(lambda p: len(p))

bd['len'] = tamanho

is_5 = bd['len'] == 5
bd_5 = bd[is_5]
bd_5.reset_index()


def segunda_letra(row):
    row.Aarao = row.Aarao[1]
    return row


second = bd_5.apply(segunda_letra, axis='columns')
second = second.Aarao
bd_5['segunda'] = second


def quarta_letra(row):
    row.Aarao = row.Aarao[3]
    return row


quart = bd_5.apply(quarta_letra, axis='columns')
quart = quart.loc[:, ['Aarao']]
bd_5['quarta'] = quart

# print(bd_5)


teste = bd_5.loc[(bd_5.segunda == 'i') & (bd_5.quarta=='u')]

print(teste)
# teste = bd_5.Aarao.map(lambda p: )

# print(bd_5)
