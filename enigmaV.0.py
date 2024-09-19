import random

ipt = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

r1s = [0,1,2,3]
r2s = [0,1,2,3]
r3s = [0,1,2,3]
minor=[3,2,1,0]

m=0
x=0

def enigma(a):
    
    pos = ipt.index(a)
    
    dico = {index: liste for index, liste in enumerate(r1s)}
    fin=dico[pos]
    
    dico = {index: liste for index, liste in enumerate(r2s)}
    fin=dico[fin]
    
    dico = {index: liste for index, liste in enumerate(r3s)}
    fin=dico[fin]
    
    dico = {index: liste for index, liste in enumerate(minor)}
    fin=dico[fin]
    
    dico = {index: liste for index, liste in enumerate(r3s)}
    fin=dico[fin]
    
    dico = {index: liste for index, liste in enumerate(r2s)}
    fin=dico[fin]
    
    dico = {index: liste for index, liste in enumerate(r1s)}
    fin=dico[fin]
    
    res = ipt[fin]
    
    #if r1s[0]==3and r2s[0]==2:
    #    r1s.append(r1s.pop(0))
    #    r2s.append(r2s.pop(0))
    #    r3s.append(r3s.pop(0))
    #elif r1s[0]==3:
    #    r1s.append(r1s.pop(0))
    #    r2s.append(r2s.pop(0))
    #else:
    #    r1s.append(r1s.pop(0))

    return res
    
    
   
#test
while x<=1000:
    x+=1
    turnr1=random.randint(0,3)
    turnr2=random.randint(0,3)
    turnr3=random.randint(0,3)
    random_index = random.randint(0,3)
    rep=ipt[random_index]

    for i in range(0,turnr1):
        r1s.append(r1s.pop(0))
    for i in range(0,turnr2):
        r2s.append(r2s.pop(0))
    for i in range(0,turnr3):
        r3s.append(r3s.pop(0))
    
    a=enigma(rep)
    if rep==enigma(a):
        print('reussie')
        True
    else:
        print("erreur")
        break