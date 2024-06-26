# Exercice 1

def parcours_largeur(a):
    parcours = []
    file = [a]

    while file:
        arbre = file.pop(0)
        parcours.append(arbre[1])

        if arbre[0] != None:
            file.append(arbre[0])

        if arbre[2] != None:
            file.append(arbre[2])

    return parcours

arbre = ( ( (None, 1, None), 2, (None, 3, None) ), 4, ( (None, 5, None), 6, (None, 7, None) ) )
assert parcours_largeur(arbre) == [4, 2, 6, 1, 3, 5, 7]

# Exercice 2

def somme_max(tab):
    n = len(tab)
    sommes_max = [0]*n
    sommes_max[0] = tab[0]
    # on calcule la plus grande somme se terminant en i
    for i in range(1,n):
        if sommes_max[i-1] + tab[i] > tab[i]:
            sommes_max[i] = sommes_max[i-1] + tab[i]
        else:
            sommes_max[i] = tab[i]
    # on en déduit la plus grande somme de celles-ci
    maximum = 0
    for i in range(1, n):
        if sommes_max[i] > sommes_max[maximum]:
            maximum = i
    return sommes_max[maximum]

assert somme_max([1, 2, 3, 4, 5]) == 15
assert somme_max([1, 2, -3, 4, 5]) == 9
assert somme_max([1, 2, -2, 4, 5]) == 10
assert somme_max([1, -2, 3, 10, -4, 7, 2, -5]) == 18
