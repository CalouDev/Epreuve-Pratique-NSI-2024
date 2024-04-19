# Exercice 1

def annee_temperature_minimale(t_moy, annees):
    resultat = (t_moy[0], annees[0])
    for i in range(1, len(t_moy)):
        if t_moy[i] < resultat[0]:
            resultat = (t_moy[i], annees[i])

    return resultat


t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
assert annee_temperature_minimale(t_moy, annees) == (12.5, 2016)

# Exercice 2

def inverse_chaine(chaine):
    '''Retourne la chaine inversée'''
    resultat = ""
    for caractere in chaine:
        resultat = caractere + resultat
    return resultat

def est_palindrome(chaine):
    '''Renvoie un booléen indiquant si la chaine ch
    est un palindrome'''
    inverse = inverse_chaine(chaine)
    return chaine == inverse

def est_nbre_palindrome(nbre):
    '''Renvoie un booléen indiquant si le nombre nbre
    est un palindrome'''
    chaine = str(nbre)
    return est_palindrome(chaine)

assert inverse_chaine('bac') == 'cab'
assert not est_palindrome('NSI')
assert est_palindrome('ISN-NSI')
assert not est_nbre_palindrome(214312)
assert est_nbre_palindrome(213312)
