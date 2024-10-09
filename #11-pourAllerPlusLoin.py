hauteur = int(input('Quelle est la hauteur du triangle ? '))

print('\n')
print('\n')

def triangle(hauteur) : 
    layer = 0
    for i in range(hauteur) : 
        layer = layer + 1
        caracter = '#' * layer
        print(f'{caracter}') 

triangle(hauteur)

print('\n')
print('\n')


def triangleIsoceleInverse(hauteur):
    for i in range(hauteur, 0, -1):
        espaces = ' ' * (hauteur - i)
        hashtags = '#' * (2 * i - 1)
        print(espaces + hashtags)
        
triangleIsoceleInverse(hauteur)    

print('\n')
print('\n')

def triangleIsocele(hauteur):
    for i in range(0, hauteur, 1):
        espaces = ' ' * (hauteur - i)
        hashtags = '#' * (2 * i - 1)
        print(espaces + hashtags)

triangleIsocele(hauteur)        