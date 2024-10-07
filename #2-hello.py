import sys

nom = sys.stdin.readline().strip()
age = int(sys.stdin.readline().strip())

anneCourante = 2024
anneeDeNaissance = anneCourante - age

print('Hello ' + nom + ', welcome to the World!')
print('Bonjour ' + nom + ' l\'apostrophe, c\'est cool !')
print('Bonjour ' + nom + ", comme diraient certains : \"quelle belle journée\" !")
print('Bonjour ' + nom + ", comme dirait l'autre : \"c'est une belle journée\"")
print(nom + ' est né en ' + str(anneeDeNaissance) + ", il y a " + str(age)) 
