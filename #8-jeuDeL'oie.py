from random import randint

nbJoueurs = int(input('Combien de joueur(s) ? '))
nbCases = 63

def randomNumber() :
    nb_aleatoire = randint(1, 6)
    return nb_aleatoire

def devinerNombre(a, b, joueur, tours):
    if a != b:
        print(f'{joueur}, vous êtes à la case {case}')
        return False
    else:
        print(f'{joueur} a gagné !. Gagné en {tours} tours.')
        return True

tours = 0
pseudo = []
c = False

for i in range(1, nbJoueurs + 1):
    response = input(f"Quel est ton pseudo (Joueur {i}) ? ")
    pseudo.append(response)

while not c:
    tours += 1  
    for i in range(nbJoueurs):
        joueurActuel = pseudo[i]
        avancementDuJoueur = randomNumber()        
        
        if devinerNombre(case, nbCases, joueurActuel, tours):
            c = True  
            break    