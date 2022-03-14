# SITE manipulação de dados: https://archive.ics.uci.edu/ml/machine-learning-databases/iris/

#basedados = []
#with open('iris.data','r') as arquivo:
 #   for registro in arquivo.readlines():
  #      basedados.append(registro.split(','))


#print(basedados)

#print(float(basedados[0][0])+ float(basedados[0][1]))


import json
#with open('bd.json','r') as arq_json:
 #   dicionario = json.load(arq_json)
  #  print(dicionario)
   # for chave,dados in dicionario.items():
    #    print(chave + ' | ' + str(dados))

dicionario = {
    "Chaves": ["CHAVES DO 8", "14/04/2022", "RECEP_01"],
    "QUICO": ["QUICO FLORES", "24/04/2022", "RAIOX_01"],
    "FLORINDA": ["DONA FLORINDA", "18/04/2022", "RECEP_03"]
}
with open('bd1.json','w') as json_file:
  json.dump(dicionario,json_file)