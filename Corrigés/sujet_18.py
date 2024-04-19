# Exercice 1

def multiplication(n1, n2):
    resultat = n2
    for _ in range(1, abs(n1)):
        resultat += n2

    return resultat if n1 > 0 else -resultat

assert multiplication(3, 5) == 15
assert multiplication(-4, -8) == 32
assert multiplication(-2, 6) == -12
assert multiplication(-2, 0) == 0

# Exercice 2

def chercher(tab, x, i, j):
    '''Renvoie l'indice de x dans tab, si x est dans tab,
    None sinon.
    On suppose que tab est trié dans l'ordre croissant.'''
    if i > j:
        return None
    m = (i + j) // 2
    if tab[m] < x:
        return chercher(tab, x, m+1 , j)
    elif tab[m] > x:
        return chercher(tab, x, i , m-1)
    else:
        return m

assert chercher([1, 5, 6, 6, 9, 12], 7, 0, 10) == None
assert chercher([1, 5, 6, 6, 9, 12], 7, 0, 5) == None
assert chercher([1, 5, 6, 6, 9, 12], 9, 0, 5) == 4
assert chercher([1, 5, 6, 6, 9, 12], 6, 0, 5) == 2