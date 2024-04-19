# Exercice 1

def moyenne(tab):
    somme_notes = 0
    somme_coeffs = 0
    for note, coeff in tab:
        somme_notes += note * coeff
        somme_coeffs += coeff
    
    return somme_notes / somme_coeffs

assert moyenne([(15.0,2),(9.0,1),(12.0,3)]) == 12.5

# Exercice 2

def ligne_suivante(ligne):
    '''Renvoie la ligne suivant ligne du triangle de Pascal'''
    ligne_suiv = [1]
    for i in range(1, len(ligne)):
        ligne_suiv.append(ligne[i-1] + ligne[i])
    ligne_suiv.append(1)
    return ligne_suiv

def pascal(n):
    '''Renvoie le triangle de Pascal de hauteur n'''
    triangle = [ [1] ]
    for k in range(n):
        ligne_k = ligne_suivante(triangle[k])
        triangle.append(ligne_k)
    return triangle

assert ligne_suivante([1, 3, 3, 1]) == [1, 4, 6, 4, 1]
assert pascal(2) == [[1], [1, 1], [1, 2, 1]]
assert pascal(3) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]