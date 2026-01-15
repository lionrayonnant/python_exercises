def calculer_moyenne(n: list) -> float:
    '''
    Permets de calculer la moyenne d'une liste.
    Entrée : liste
    Sortie : float
    '''

    tot = 0
    for val in n:
        tot += val

    moy = x / len(n)
    return moy

list1 = [1,2]
print(calculer_moyenne(list1))