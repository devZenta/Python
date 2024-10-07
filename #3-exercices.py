from math import pi

def perimetreCercle(r): 
    return 2 * pi * r

def vitesseCoureur(distance, temps): 
    return distance / temps * 3.6

def longueurPisteCourse(r, l):
    LongueurCercle = perimetreCercle(r)
    longueurLigneDroite = (2 * l) 
    longueurFinale = longueurLigneDroite + LongueurCercle
    return longueurFinale

def vitesseMoyenne(l, r, t):   
    return vitesseCoureur(longueurPisteCourse(l, r), t)

def vitesseMoyenneManyCoureurs() : 
    l = int(input('Quelle est la longeur de la piste ? '))
    r = int(input('Quel est le rayon du cercle ? '))
    coureurs = int(input('Combien de coureurs ? '))
    distance = longueurPisteCourse(r, l)
    vitesse = []
    sommeVitesse = 0
    for i in range(0, coureurs) :
        time = int(input('Quel est votre temps ? '))
        result = vitesseCoureur(distance, time)
        vitesse.append(result)
        sommeVitesse = sommeVitesse + result
    vitesseMoyenneCoureurs = sommeVitesse / len(vitesse)
    return 'Voici la vitesse moyenne des ' + str(coureurs) + ' coureurs : ' + str(vitesseMoyenneCoureurs)

print(vitesseMoyenneManyCoureurs())












