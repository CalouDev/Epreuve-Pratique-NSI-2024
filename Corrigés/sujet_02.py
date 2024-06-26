# Exercice 1

def correspond(mot, mot_a_trous):
    if len(mot) != len(mot_a_trous):
        return False
    for i in range(len(mot)):
        if mot[i] != mot_a_trous[i] and mot_a_trous[i] != '*':
            return False
    return True

assert correspond('INFORMATIQUE', 'INFO*MA*IQUE')
assert not correspond('AUTOMATIQUE', 'INFO*MA*IQUE')
assert not correspond('STOP', 'S*')
assert correspond('AUTO', '*UT*')

# Exercice 2

def est_cyclique(plan):
    '''Prend en paramètre un dictionnaire `plan` correspondant à
    un plan d'envoi de messages (ici entre les personnes A, B, C,
    D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et
    False sinon.'''
    expediteur = 'A'
    destinataire = plan[expediteur]
    nb_destinataires = 1
    while destinataire != expediteur:
        destinataire = plan[destinataire]
        nb_destinataires = nb_destinataires + 1
    return nb_destinataires == len(plan)

assert not est_cyclique({'A':'E','F':'A','C':'D','E':'B','B':'F','D':'C'})
assert est_cyclique({'A':'E','F':'C','C':'D','E':'B','B':'F','D':'A'})
assert est_cyclique({'A':'B','F':'C','C':'D','E':'A','B':'F','D':'E'})
assert not est_cyclique({'A':'B','F':'A','C':'D','E':'C','B':'F','D':'E'})
