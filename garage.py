class Vehicule:
    def __init__(self,marque: str, modele: str, annee: int):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def afficher_infos(self):
        return f"{self.marque}, {self.modele}, {self.annee}\n"
    
    def demarrer(self):
        return f"Le véhicule démarre"
    
class Voiture(Vehicule):
    def __init__(self,marque: str, modele: str, annee: int, nb_portes : int):
        Vehicule.__init__(self, marque, modele, annee)
        self.nb_portes = nb_portes

    def afficher_nb_portes(self):
        return f"Cette voiture a {self.nb_portes} portes.\n"
    
    def demarrer(self):
        return f"La {self.modele} fait vroom"
    
class Moto(Vehicule):
    def __init__(self,marque: str, modele: str, annee: int, cylindree: int):
        Vehicule.__init__(self, marque, modele, annee)
        self.cylindree = cylindree
    
    def afficher_cylindree(self):
        return f"Cette moto a une cylindrée de {self.cylindree} cm^3.\n"

    def demarrer(self):
        return f"La {self.modele} fait bop-bop-bop"
    
volvo480 = Voiture("Volvo", "480", 1986, 5)
r6 = Moto("Yamaha", "R6 RACE", 2025, 600)

print(volvo480.afficher_infos())
print(volvo480.afficher_nb_portes())

print(r6.afficher_infos())
print(r6.afficher_cylindree())

print(volvo480.demarrer())
print(r6.demarrer())