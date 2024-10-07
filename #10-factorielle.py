entree = int(input('Quelle factorielle ? '))

def factResult(n) :
    if n == 1 :
        return 1
    elif n < 1 :
        return 'Pas de factorielle'
    else :
        return n * factResult(n-1)

print(factResult(entree))


longueurTableau = int(input('Combien d\'élément dans le tableau ? '))
valeursTableau = []

for i in range(0, longueurTableau) : 
    valeurs = int(input(f'Valeurs {i + 1} : '))
    valeursTableau.append(valeurs)

def sommeRecursive(tableau) : 
    if len(tableau) == 0 : 
        return 0
    return tableau[len(tableau)-1] + sommeRecursive((tableau[0:-1]))

print(sommeRecursive(valeursTableau))

def triNaifIteratif(tab):
    """
    Trie un tableau sur place à l'aide du tri naif : cherche le plus petit élément et le met en
    tête du tableau, puis le plus petit suivant, etc
    """
    # Pour chaque taille du tableau (on élimie à chaque itération le 1er élément)
    for i in range(0,len(tab)):
        # Trouver le plus petit élément
        min = tab[i]
        indexMin = i
        for c in range(i,len(tab)):
            if tab[c] < min:
                indexMin = c
                min = tab[c]
        

        # Ramener le plus petit élément en 1ere position
        # Swap l'élément i avec l'élément j
        tab[i],tab[indexMin] = tab[indexMin],tab[i]
        # (code équivalent à celui-ci :)
        # temp = tab[i]
        # tab[i] = tab[j]
        # tab[j] = temp


def triRapideRecursif(tab):
    """
    Renvoie un tableau trié
    Recursion :
        - Pivot : 1er élément du tableau
        - construit deux sous tableau :
            - tous les elts plus petits que le pivot
            - tous les elts plus grand ou égal que le pivot
        - 2 appels recursifs sur les deux sous tableaux
        - résultat : concaténation sousTableau1 + pivot + sousTableau2
    Condition limite : tableau de 1 element ou 0 élement est déjà trié
    """
    # Condition limite
    if len(tab) <= 1:
        return tab
    
    pivot = tab[0]
    sousTableau1 = []
    sousTableau2 = []
    for elt in tab[1:]:
        # Remplissage des deux sous tableau
        if elt < pivot:
            sousTableau1.append(elt)
        else:
            sousTableau2.append(elt)
    # Appels recursifs sur les deux sous tableaux
    sousTableau1 = triRapideRecursif(sousTableau1)
    sousTableau2 = triRapideRecursif(sousTableau2)

    # Reconstituer le tableau final
    return sousTableau1 + [pivot] + sousTableau2


tableauTest1 = [1,5,3,5,6,7,3,4,5]
tableauTest2 = [1,5,3,5,6,7,3,4,5]

triNaifIteratif(tableauTest1)
print(tableauTest1)

tableauTest2 = triRapideRecursif(tableauTest2)
print(tableauTest2)



