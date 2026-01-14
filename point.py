'''
Ecrire une classe Point contenant 
4 variables
◦ x : l’axe des abscisses 
◦ y : l’axe des ordonnées 
◦ Nom : nom du point
◦ dist_xy : la distance entre x et y
◦ Un constructeur qui initialisera les trois variables. Les valeurs de x et y seront passées en 
paramètre
◦ Une fonction __str__() qui renverra les valeurs des paramètres du point
On testera la classe avec le point A(10,20)

'''

import math

class Point:
    def __init__(self,n,x,y):
        self.name = n
        self.x = x
        self.y = y
        self.dist_xy = (x**2 + y**2)**0.5

    def __str__(self):
        return f"{self.name} ; x = {self.x} ; y = {self.y} ; distance xy : {self.dist_xy}\n"
    
#A = Point("A",10,20)
#print(f"{A}")

'''

Ecrire une classe Triangle constituée de 
▪3 points A,B,C 
▪ D’un constructeur qui créera les trois points
▪ D’une fonction __str__() qui affichera les trois points
On testera la classe avec les points A(1,1), B(2,4), C(6,9)

'''

'''

On veut ajouter deux fonctions 
▪Segments() : qui renvoie la taille de tous les segments
▪Aire() : qui calcule l’aire du triangle
On testera la classe avec les points A(1,1), B(2,4), C(6,9)

'''

class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"{self.a}{self.b}{self.c}"

    def segments(self):
        def dist(p,q):
            x = math.sqrt(((q.x - p.x)**2)+((q.y - p.y)**2))
            return x

        AB = dist(self.a, self.b)
        BC = dist(self.b, self.c)
        CA = dist(self.c, self.a)
        return AB, BC, CA
    
    def aire(self):
        AB, BC, CA = self.segments()
        # utilisation de la formule de Héron
        p = (AB + BC + CA)/2 # demi périmètre en cm
        A = (math.sqrt(p*(AB)*(BC)*(CA))) # aire en cm^2
        return f"{A}"
    
# Définition du triangle avec la classe Triangle
tr = Triangle(Point("A",1,1),Point("B",2,4),Point("C",6,9))

print(f"Coordonées du triangle :\n")
print(tr)
print(f"Segments du triangle :\n")
print(tr.segments())
print("Aire du triangle :\n")
print(tr.aire())