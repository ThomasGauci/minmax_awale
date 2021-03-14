import numpy as np

score = np.full(2,0)
print("initialisation : ")
plateau = np.full(24,6)
print(plateau)
print("-------------------------------------------------")


def jouer(joueur,case):
    if joueur > 2 or case > 24:
        print("erreur : case ou joueur non existant")
    else:
        if plateau[case] == 0:
              print("erreur : coup illegal - case vide")
        else:
            if joueur == 1:
                if case % 2 == 0:
                    print("erreur : coup illegal - case paire")
                else:
                    coup(joueur,case)
            if joueur == 2:
                if case % 2 != 0:
                    print("erreur : coup illegal - case impaire")
                else:
                    coup(joueur,case)

def coup(joueur,case):    
    lastCase = case
    for x in range(1,plateau[case]+1):
        plateau[(case+x)%24]=plateau[(case+x)%24]+1
        lastCase = (case+x)%24
    check_derniere_case(joueur,lastCase)
    plateau[case] = 0
    print(plateau)

# 1) quand il met sa graine dans la dernière case et qu'il reste 2 ou 3 graines dans la case
# 2) soit par rammassage: si tu as pris les pions dans une case, alors tu regarde la case precedente, si elle contient 2 ou 3 pions alors tu prend les pions de la case et tu repetes le raisnnement
def check_derniere_case(joueur,case):
    if(plateau[(case)%24] == 2 or plateau[(case)%24] == 3):
        score[joueur-1] += plateau[(case)%24]
        plateau[(case)%24] = 0
        check_ramassage(joueur,case-1)

def check_ramassage(joueur,case):
    if(plateau[(case)%24] == 2 or plateau[(case)%24] == 3):
        score[joueur-1] += plateau[(case)%24]
        plateau[(case)%24] = 0  
        check_ramassage(joueur,case)     


jouer(1,21)     #joueur 1 case 21
jouer(2,6)      #joueur 2 case 6
jouer(1,25)     #joueur 1 case inexistante
jouer(1,6)      #joueur 1 case illegal - case vide
jouer(1,8)      #joueur 1 case illegal - case pair
#print(score)
