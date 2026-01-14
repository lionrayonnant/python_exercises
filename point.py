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

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.dist_xy = (x**2 + y**2)**0.5

    def __str__(self):
        return f"x = {self.x} ; y = {self.y} ; distance xy : {self.dist_xy}\n"
    
A = Point(10,20)
print(f"A : {A}")

'''

Ecrire une classe Triangle constituée de 
▪3 points A,B,C 
▪ D’un constructeur qui créera les trois points
▪ D’une fonction __str__() qui affichera les trois points
On testera la classe avec les points A(1,1), B(2,4), C(6,9)

'''

class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"A : {self.a}B : {self.b}C : {self.c}"
    
tr = Triangle(Point(1,1),Point(2,4),Point(6,9))
print(tr)

