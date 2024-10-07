from random import randint

limit = int(input('Choisissez l\'intervalle du nombre aléaroire [1,...] : '))
nombreJoueurs= int(input('Combien de joueurs ? '))
print('L\'intervalle est donc [1, ' + str(limit) + ']')

def randomNumber() :
    nb_aleatoire = randint(1, limit)
    return nb_aleatoire

def devinerNombre(a, b, joueur, tours):
    if a > b:
        print(f'{joueur}, c\'est plus bas')
        return False
    elif a < b:
        print(f'{joueur}, c\'est plus haut')
        return False
    else:
        print(f'{joueur} a gagné ! Le nombre correct était {b}. Trouvé en {tours} tours.')
        return True  

def enterNumber(joueur):
    return int(input(f'{joueur}, entre une proposition de nombre : ')) 

x = randomNumber()
tours = 0
c = False
pseudo = []

for i in range(1, nombreJoueurs + 1):
    response = input(f"Quel est ton pseudo (Joueur {i}) ? ")
    pseudo.append(response)

while not c:
    tours += 1  
    for i in range(nombreJoueurs):
        joueur_actuel = pseudo[i]
        print(f'Au tour de {joueur_actuel}')
        y = enterNumber(joueur_actuel)
        
        if devinerNombre(y, x, joueur_actuel, tours):
            c = True  
            break 

        