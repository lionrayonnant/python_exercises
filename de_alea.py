'''

1. Ecrire une classe dé avec un constructeur qui crée un dé à n faces.
2. Ajouter une methode tirer_de(self,n) renvoyant un nombre 
aléatoire entre 1 et n (n étant le nombre de faces du dé). On utilisera la 
fonction randint du module random
3. Ajouter une methode __str__() qui affiche le dé 
4. Ecrire une classe trois_des avec un constructeur qui tire trois dés et une 
méthode __str__()qui affiche les trois dés 

'''

import random

class de:
    def __init__(self,name):
        n = 6
        self.name = name

    def tirer_de(self):
        alea = random.randint(1,6)
        return alea
    
    def __str__(self):
        return f"{self.name} vaut {self.tirer_de()}."

class trois_de:
    def __init__(self, a, b, c):
        self.a = de(a)
        self.b = de(b)
        self.c = de(c)

    def __str__(self):
        return f"{self.a} ; {self.b} ; {self.c}"
    
des = trois_de("A","B","C")
print(des)
