import numpy as np

score = np.full(2,0)
plateau = np.full(24,6)
plateauGain = np.full(24,0)

def jouer(joueur,case,plateau):
    if joueur > 1 | case > 24:
        print("erreur : case ou joueur non existant")
    else:
        if plateau[case] == 0:
              print("erreur : coup illegal")
        else:
            if joueur == 1:
                if case % 2 != 0:
                    print("erreur : coup illegal j1")
                else:
                    print("Le joueur 1 joue la case : " + str(case) + " avec " + str(plateau[case]) + " graines")
                    coup(joueur,case,plateau)
            if joueur == 2:
                if case % 2 == 0:
                    print("erreur : coup illegal j2")
                else:
                    print("Le joueur 2 joue la case : " + str(case) + " avec " + str(plateau[case]) + " graines")
                    coup(joueur,case,plateau)
    
    #print(plateau)git

def coup(joueur,case,plateau):    
    lastCase = case
    for x in range(1,plateau[case]+1):
        plateau[(case+x)%24]=plateau[(case+x)%24]+1
        lastCase = (case+x)%24
    check_derniere_case(joueur,lastCase,plateau)
    plateau[case] = 0

# 1) quand il met sa graine dans la dernière case et qu'il reste 2 ou 3 graines dans la case
# 2) soit par rammassage: si tu as pris les pions dans une case, alors tu regarde la case precedente, si elle contient 2 ou 3 pions alors tu prend les pions de la case et tu repetes le raisnnement

def check_derniere_case(joueur,case,plateau):
    if(plateau[(case)%24] == 2 or plateau[(case)%24] == 3):
        score[joueur-1] += plateau[(case)%24]
        plateau[(case)%24] = 0
        check_ramassage(joueur,case-1,plateau)

def check_ramassage(joueur,case,plateau):
    if(plateau[(case)%24] == 2 or plateau[(case)%24] == 3):
        score[joueur-1] += plateau[(case)%24]
        plateau[(case)%24] = 0  
        check_ramassage(joueur,case,plateau)     

def min_max(plateau,joueur,profondeur):
    print("--------------------------------------------------------------")
    c = profondeur - 1
    meilleurCoup = -1
    p = 0
    d = 0
    if c != 0:
        for i in range(len(plateau)-1):
            plateauMinMax = []
            plateauMinMax.extend(plateau)
            if joueur == 1:
                if plateauMinMax[i] != 0 and i%2 == 0 :
                    jouer(1,i,plateauMinMax)
                    print(plateauMinMax)
                    print("Score : " + str(score[0]) + " " + str(p) )
                    if score[0] > p:
                        p = score[0]
                        meilleurCoup = i
                    score[0] = 0
                    d = min_max(plateauMinMax,2,c)
            else :
                if plateauMinMax[i] != 0 and i%2 != 0 :
                    jouer(2,i,plateauMinMax)
                    print(plateauMinMax)
                    print("Score : " + str(-score[1]) + " " + str(p) )
                    if -score[1] < p:
                        p = -score[1]
                        meilleurCoup = i
                    score[1] = 0
                    d = min_max(plateauMinMax,2,c)
        print("Gain plateau : " + str(p) + " valeur des descendants : " + str(d))
    if profondeur == 3:
        print("Meilleur coup : " + str(meilleurCoup))
    return p - d
    
# Joueur 1 commence
plateauInit = [6,6,6,6,6,6,2,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]
min_max(plateauInit,1,3)

# faire fin du jeu