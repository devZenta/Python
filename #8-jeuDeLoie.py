from random import randint

nbJoueurs = int(input('Combien de joueur(s) ? '))
nbCases = 63

def randomNumber() :
    nb_aleatoire = randint(1, 6)
    return nb_aleatoire

def verifierVictoire(position, joueur, tours):
    if position == nbCases:
        print(f'{joueur} a gagné ! Gagné en {tours} tours.')
        return True
    else:
        return False

def afficherPlateau(pseudo, positions):
    print("\n--- Plateau de jeu ---")
    for i in range(len(pseudo)):
        print(f'{pseudo[i]} est à la case {positions[i]}')
    print("----------------------\n")

tours = 0
pseudo = []
positions = [0] * nbJoueurs 
c = False  

for i in range(1, nbJoueurs + 1):
    response = input(f"Quel est ton pseudo (Joueur {i}) ? ")
    pseudo.append(response)

while not c:
    tours += 1  
    print(f"\n=== Tour {tours} ===")
    
    for i in range(nbJoueurs):
        joueurActuel = pseudo[i]

        input(f"{joueurActuel}, appuie sur Entrée pour lancer le dé...")
        
        avancementDuJoueur = randomNumber()
        positions[i] += avancementDuJoueur

        if positions[i] > nbCases :
            surplus = positions[i] - nbCases
            positions[i] = nbCases - surplus 
        
        print(f'{joueurActuel} a lancé un {avancementDuJoueur} et avance à la case {positions[i]}')

        if verifierVictoire(positions[i], joueurActuel, tours):
            c = True  
            break  

    afficherPlateau(pseudo, positions)    
