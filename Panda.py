import pandas as edu
divisor = ("-="*40)

#Questão 2
print('A extensão dos arquivos é CSV.')
print(divisor)

#QUESTÃO 3
print('Os arquivos contém informações de artistas, faixas, popularidade, playlists entre outras coisas.')
print(divisor)

alternative = edu.read_csv("alternative_music_data.csv")
blues = edu.read_csv("blues_music_data.csv")
hiphop = edu.read_csv("hiphop_music_data.csv")

#Questão 5
print(f'A base de dados "Alternative Music" possui a dimensão {alternative.shape}.\nA base de dados "Blues Music" possui a dimensão {blues.shape}.\nA base de dados "HipHop Music" possui a dimensão {hiphop.shape}.')
print(divisor)

#QUESTÃO 6
print(f'Os nomes das colunas são:\n{alternative.columns}')
print(divisor)

#Questão 7
print(f'Os tipos de dados de cada coluna são:\n{alternative.dtypes}')
print(divisor)

#Questão 8
alternative ["Coluna_Nova"] = 1
print(f'Com a coluna nova, agora a base de dados "Alternative Music" possue a dimensão {alternative.shape}.')

#Questão 9
blues ["Coluna_Nova"] = 2
print(f'Com a coluna nova, agora a base de dados "Blues Music" possue a dimensão {blues.shape}.')

#Questão 10
hiphop ["Coluna_Nova"] = 3
print(f'Com a coluna nova, agora a base de dados "HipHop Music" possue a dimensão {hiphop.shape}.')

print(divisor)
#Questão 11
arquivo_completo = edu.concat([alternative,blues,hiphop],ignore_index=True)

#QUESTÕES 12 E 13
print(f'Não existem entradas com valores "NaN" no DataFrame.\nSua contagem segue abaixo:\n{arquivo_completo.isnull().sum()}')
print(divisor)

#QUESTÃO 14
arquivo_completo_nostring = arquivo_completo.select_dtypes(exclude=['object'])
print(f'Após a remover colunas que continham strings,o Dataframe ficou com as dimensões {arquivo_completo_nostring.shape}\ne restaram as seguintes colunas:\n{arquivo_completo_nostring.dtypes}')

arquivo_completo_nostring.to_csv('arquivo_completo.csv')


















