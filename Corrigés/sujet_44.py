# Exercice 1

def enumere(tab):
    resultat = {}
    for i in range(len(tab)):
        if tab[i] in resultat:
            resultat[tab[i]].append(i)
        else:
            resultat[tab[i]] = [i]

    return resultat

assert enumere([]) == {}
assert enumere([1, 2, 3]) == {1: [0], 2: [1], 3: [2]}
assert enumere([1, 1, 2, 3, 2, 1]) == {1: [0, 1, 5], 2: [2, 4], 3: [3]}

# Exercice 2

class Noeud:
    """Classe représentant un noeud d'un arbre binaire"""
    def __init__(self, etiquette, gauche, droit):
        """Crée un noeud de valeur etiquette avec
        gauche et droit comme fils."""
        self.etiquette = etiquette
        self.gauche = gauche
        self.droit = droit

def parcours(arbre, liste):
    """parcours récursivement l'arbre en ajoutant les étiquettes
    de ses noeuds à la liste passée en argument en ordre infixe."""
    if arbre != None:
        parcours(arbre.gauche, liste)
        liste.append(arbre.etiquette)
        parcours(arbre.droit, liste)
    return liste

def insere(arbre, cle):
    """insere la cle dans l'arbre binaire de recherche
    représenté par arbre.
    Retourne l'arbre modifié."""
    if arbre == None:
        return Noeud(cle, None, None) # creation d'une feuille
    else:
        if cle < arbre.etiquette:
            arbre.gauche = insere(arbre.gauche, cle)
        else:
            arbre.droit = insere(arbre.droit, cle)
    return arbre

a = Noeud(5, None, None)
a = insere(a, 2)
a = insere(a, 3)
a = insere(a, 7)
assert parcours(a, []) == [2, 3, 5, 7]
a = insere(a, 1)
a = insere(a, 4)
a = insere(a, 6)
a = insere(a, 8)
assert parcours(a, []) == [1, 2, 3, 4, 5, 6, 7, 8]