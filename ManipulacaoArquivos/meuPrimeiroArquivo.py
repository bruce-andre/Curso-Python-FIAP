#arquivo= open('primeiro_arquivo.txt','w')

#arquivo.write('Meu primeiro arquivo !')

#arquivo.close()

#with open('primeiro_arquivo.txt','a') as arquivo: #a = inclui no arquivo // w = cria o arquivo
    #arquivo.write('\nTentativa 3')

with open('primeiro_arquivo.txt','r') as arquivo:

    for linha in arquivo.readlines(): # para ver o arquivo linha a linha
        print(linha)
