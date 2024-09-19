ipt = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

r1s = [0, 24, 17, 3, 9, 14, 23, 18, 1, 13, 22, 8, 20, 16, 6, 15, 11, 4, 21, 10, 5, 7, 2, 19, 25, 12]
r2s = [23, 17, 2, 11, 22, 24, 13, 9, 12, 5, 21, 25, 14, 10, 0, 1, 4, 15, 16, 20, 3, 6, 18, 8, 19, 7]
r3s = [14, 4, 23, 12, 24, 3, 22, 16, 11, 0, 19, 17, 9, 6, 2, 8, 7, 13, 15, 1, 20, 5, 10, 18, 21, 25]
minor=[11, 25, 17, 8, 15, 23, 14, 3, 19, 5, 6, 0, 9, 18, 7, 4, 21, 2, 13, 10, 12, 16, 24, 22, 20, 1]

m=0

def enigma(a):
    
    pos = ipt.index(a)
    #print(pos,"#notwrong")
    
    dico = {index: liste for index, liste in enumerate(r1s)}
    fin=dico[pos]
    #print(fin, "#1")
    
    dico = {index: liste for index, liste in enumerate(r2s)}
    fin=dico[fin]
    #print(fin, "#2")
    
    dico = {index: liste for index, liste in enumerate(r3s)}
    fin=dico[fin]
    #print(fin, "#3")
    
    dico = {index: liste for index, liste in enumerate(minor)}
    fin=dico[fin]
    #print(fin, "#4")
    
    dico = {index: liste for index, liste in enumerate(r3s)}
    fin=dico[fin]
    #print(fin, "#5")
    
    dico = {index: liste for index, liste in enumerate(r2s)}
    fin=dico[fin]
    #print(fin, "#6")
    
    dico = {index: liste for index, liste in enumerate(r1s)}
    fin=dico[fin]
    #print(fin, "#7")
    
    res = ipt[fin]
    
    if r1s[0]==3 and r2s[0]==2:
        r1s.append(r1s.pop(0))
        r2s.append(r2s.pop(0))
        r3s.append(r3s.pop(0))
    elif r1s[0]==3:
        r1s.append(r1s.pop(0))
        r2s.append(r2s.pop(0))
    else:
        r1s.append(r1s.pop(0))

    return res
    
turnr1=int(input())
turnr2=int(input())
turnr3=int(input())
rep = list(input())


for i in range(0,turnr1):
    r1s.append(r1s.pop(0))
for i in range(0,turnr2):
    r2s.append(r2s.pop(0))
for i in range(0,turnr3):
    r3s.append(r3s.pop(0))

for i in rep:
    a=enigma(i)
    print(a)

#print(r1s)
#print(r2s)
#print(r3s)
#print(rep)
#print(enigma(rep))
#print(r1s)
#print(r2s)
#print(r3s)





#seklcfè etfxciotxfbèi cb               AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA