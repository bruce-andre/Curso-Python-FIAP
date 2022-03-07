usuarios = {}
print (usuarios)

usuarios = {
    'chaves' : ['Chaves do 8', '24/12/2022','Recep_01'],
    'quico' : ['Quico das flores', '20/12/2022','Raiox_03']
}
print(usuarios)

usuarios['florinda'] = ['Dona Florinda', '24/12/2022', 'Raiox_01']

print(usuarios)

print('----'*45)
print(usuarios.get('quico'))