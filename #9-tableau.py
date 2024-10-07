def entreeTableau() :
 
    tab = []

    while True :
        try : 
            valeur = int(input('Entre une valeur numérique : '))
            tab.append(valeur)
        except ValueError :
            print('Error : ce n\'est pas une valeur numérique')
            break    

    return tab   

print(entreeTableau())