import numpy as np
import time
import pandas as pd

score = np.full(2,0)
scoreMinMax = np.full(2,0)
plateau = np.full(24,4)
plateauGain = np.full(24,0)

def jouer(joueur,case,plateau,minmax):
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
                    #print("Le joueur 1 joue la case : " + str(case) + " avec " + str(plateau[case]) + " graines")
                    coup(joueur,case,plateau,minmax)
            if joueur == 2:
                if case % 2 == 0:
                    print("erreur : coup illegal j2")
                else:
                    #print("Le joueur 2 joue la case : " + str(case) + " avec " + str(plateau[case]) + " graines")
                    coup(joueur,case,plateau,minmax)
    
    #print(plateau)git

def coup(joueur,case,plateau,minmax):    
    lastCase = case
    for x in range(1,plateau[case]+1):
        plateau[(case+x)%24]=plateau[(case+x)%24]+1
        lastCase = (case+x)%24
    check_derniere_case(joueur,lastCase,plateau,minmax)
    plateau[case] = 0

# 1) quand il met sa graine dans la dernière case et qu'il reste 2 ou 3 graines dans la case
# 2) soit par rammassage: si tu as pris les pions dans une case, alors tu regarde la case precedente, si elle contient 2 ou 3 pions alors tu prend les pions de la case et tu repetes le raisnnement

def check_derniere_case(joueur,case,plateau,minmax):
    if(plateau[(case)%24] == 2 or plateau[(case)%24] == 3):
        if minmax:
            scoreMinMax[joueur-1] += plateau[(case)%24]
        else:
            score[joueur-1] += plateau[(case)%24]
        plateau[(case)%24] = 0
        check_ramassage(joueur,case-1,plateau,minmax)

def check_ramassage(joueur,case,plateau,minmax):
    if(plateau[(case)%24] == 2 or plateau[(case)%24] == 3):
        if minmax:
            scoreMinMax[joueur-1] += plateau[(case)%24]
        else:
            score[joueur-1] += plateau[(case)%24]
        plateau[(case)%24] = 0  
        check_ramassage(joueur,case,plateau,minmax)     

def min_max(plateauMinMax,joueur,profondeur):
    #print("--------------------------------------------------------------")
    c = profondeur - 1
    p = 0
    d = 0
    meilleurCoup = 0
    if c != 0:
        for i in range(len(plateau)-1):
            plateauMinMax = []
            plateauMinMax.extend(plateau)
            if joueur == 1:
                if plateauMinMax[i] != 0 and i%2 == 0 :
                    while plateau[meilleurCoup] == 0:
                        meilleurCoup += 2
                    jouer(1,i,plateauMinMax,True)
                    #print(plateau)
                    #print("Score : " + str(score[0]) + " " + str(p) )
                    if scoreMinMax[0] > p:
                        p = scoreMinMax[0]
                        meilleurCoup = i
                    scoreMinMax[0] = 0
                    d = min_max(plateauMinMax,2,c)
            else :
                if plateauMinMax[i] != 0 and i%2 != 0 :
                    meilleurCoup = 1
                    while plateau[meilleurCoup] == 0:
                        meilleurCoup += 2
                    jouer(2,i,plateauMinMax,True)
                    #print(plateau)
                    #print("Score : " + str(-score[1]) + " " + str(p) )
                    if -scoreMinMax[1] < p:
                        p = -scoreMinMax[1]
                        meilleurCoup = i
                    scoreMinMax[1] = 0
                    d = min_max(plateauMinMax,1,c)
        #print("Gain plateau : " + str(p) + " valeur des descendants : " + str(d))
    if profondeur == 4:
        print(str(meilleurCoup+1),end='')
    return meilleurCoup #je renvoie le meilleur coup ducoup
    
# Joueur 1 commence
#plateauInit = [6,6,6,6,6,6,2,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]
plateauInit = [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
#min_max(plateauInit,1,3)

"""
for x in range (10):
    print(plateau)
    jouer(1,min_max(plateau,1,4),plateau)
    jouer(2,min_max(plateau,2,4),plateau)
    print(score)
"""


def separerPlateau(plateau):
    arrayj1 = []
    arrayj2 = []
    indices = []
    for x in range(len(plateau)):
        if x%2!=1:
            arrayj1.append(plateau[x])
        else:
            arrayj2.append(plateau[x])

    indices.append(arrayj1)
    indices.append(arrayj2)
    indices.append(["13","14","15","16","17","18","19","21","22","23","24","25"])
    dfj1 = pd.DataFrame(indices, index=["","",""], columns=["01","02","03","04","05","06","07","08","09","10","11","12"])
    print(dfj1)


while 1:
    print("====================================================")
    print("-------------------------------------------------")
    separerPlateau(plateau)
    print("-------------------------------------------------")
    print("coup j1 : ",end='')
    start_time = time.time()
    jouer(1,min_max(plateau,1,4),plateau,False)
    print("  (%s s)" % round(time.time() - start_time,2))
    c2 = input("coup j2 : ")
    jouer(2,int(c2)-1,plateau,False)
    print(score)
# faire fin du jeu