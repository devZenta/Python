def estPair(x) : 
    if x % 2 == 0 :
        print("Le nombre est pair")
        return True
    else :
        print('Le nombre est impair')   
        return False 
    
def max(a, b) : 
    if a > b :
        return a
    else :
        return b

def tousLesPairs(x) :
    for i in range(x + 1) :
        if i % 2 == 0:
            print(i)

def estPremier(x):
    if x < 2:
        return False
    
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
            
    return True  

def factorielle(n):
    if n < 0:
        return "La factorielle n'est pas définie pour les nombres négatifs"
    
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorielle(5)) 

