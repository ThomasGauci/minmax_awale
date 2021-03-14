import numpy as np


plateau = np.full(24,6)
print(plateau)


def jouer(joueur,case):
    if joueur >1 | case > 24:
        print("erreur : case ou joueur non existant")
    else:
        if joueur == 1:
            if case % 2 == 0:
                print("erreur : coup illegal")
            else:
                coup(case)
        if joueur == 2:
            if case % 2 != 0:
                print("erreur : coup illegal")
            else:
                coup(case)
    
    print(plateau)

def coup(case):
    plateau[case]=0
    for x in range(1,7):
        plateau[(case+x)%24]=plateau[(case+x)%24]+1

jouer(1,21)
jouer(2,22)
