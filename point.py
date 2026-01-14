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
    def __init__(self,n,x,y):
        self.name = n
        self.x = x
        self.y = y
        self.dist_xy = (x**2 + y**2)**0.5

    def __str__(self):
        return f"{self.name} : x = {self.x} ; y = {self.y} ; distance xy : {self.dist_xy}"
    
A = Point("A",10,20)
print(A)

