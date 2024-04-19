# Exercice 1

def fibonacci(n):
    n0 = 0
    n1 = 1
    for _ in range(n):
        temp = n1
        n1 += n0
        n0 = temp

    return n0

assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(25) == 75025

# Exercice 2

def eleves_du_mois(eleves, notes):
    note_maxi = 0
    meilleurs_eleves = []
    for i in range(len(eleves)):
        if notes[i] == note_maxi:
            meilleurs_eleves.append(eleves[i])
        elif notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleurs_eleves = [eleves[i]]
    return (note_maxi, meilleurs_eleves)

eleves_nsi = ['a','b','c','d','e','f','g','h','i','j']
notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]
assert eleves_du_mois(eleves_nsi, notes_nsi) == (80, ['c', 'f', 'h'])
assert eleves_du_mois([],[]) == (0, [])