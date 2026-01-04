for i in range(3):
    parola = input('Introduceti parola: ')
    while parola != 'admin':
        print('Error')
        break
    if parola == 'admin' :
        print('Grant Acces')
        break
else:
    print('Prea multe incercari! Asteptati o ora!')