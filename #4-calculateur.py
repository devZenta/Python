from math import*

print("+-----------------------------------------------------------+")
print("+                  CALCULATEUR PUISSANT                     +")
print("+-----------------------------------------------------------+")

def saisirFirstEntier() :
    chiffre = int(input("Entrez le premier chiffre : "))
    return  chiffre

n1 = saisirFirstEntier()

def saisirSecondEntier() :
    chiffre = int(input("Entrez le second chiffre  : "))
    return  chiffre

n2 = saisirSecondEntier()

def calculs(a, b) : 
    somme = a + b
    print('Somme      : ' + str(a) + ' + ' + str(b) + ' = ' + str(somme))
    difference = a - b
    print('Différence : ' + str(a) + ' - ' + str(b) + ' = ' + str(difference))
    produit = a * b
    print('Produit    : ' + str(a) + ' * ' + str(b) + ' = ' + str(produit))
    if b != 0 :
        division = a / b
        print('Division   : ' + str(a) + ' / ' + str(b) + ' = ' + str(division))    

calculs(n1, n2)
