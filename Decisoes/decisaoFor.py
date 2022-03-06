tabuada=int(input('Digite um número para exibir a tabuada: '))
print('Tabuada do número ', tabuada)
for valor in range(0,11,1): # 0 = * x 0 // 11 = limite(limite 10) // 1 = proximo numero * x 1, * x 2
    print(str(tabuada) + ' x ' + str(valor) + ' = ' + str((tabuada*valor)))