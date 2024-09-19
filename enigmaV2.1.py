ipt = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

r1s = [3,1,0,2]
r2s = [2,3,0,1]
r3s = [0,3,1,2]
minor=[1,0,2,3]

m=0

def e(a):
    
    pos = ipt.index(a)
    print(pos,"#1")
    
    dico = {index: liste for index, liste in enumerate(r1s)}
    fin=dico[pos]
    print(fin, "#2")
    
    dico = {index: liste for index, liste in enumerate(r2s)}
    fin=dico[fin]
    print(fin, "#3")
    
    dico = {index: liste for index, liste in enumerate(r3s)}
    fin=dico[fin]
    print(fin, "#4")
    
    dico = {index: liste for index, liste in enumerate(minor)}
    fin=dico[fin]
    print(fin, "#5")
    
    dico = {index: liste for index, liste in enumerate(r3s)}
    fin=dico[fin]
    print(fin, "#6")
    
    dico = {index: liste for index, liste in enumerate(r2s)}
    fin=dico[fin]
    print(fin, "#7")
    
    dico = {index: liste for index, liste in enumerate(r1s)}
    fin=dico[fin]
    print(fin, "#8")
    
    res = ipt[fin]
    
    if r1s[0]==3and r2s[0]==2:
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
rep=input()

for i in range(0,turnr1):
    r1s.append(r1s.pop(0))
for i in range(0,turnr2):
    r2s.append(r2s.pop(0))
for i in range(0,turnr3):
    r3s.append(r3s.pop(0))


print(r1s)
print(r2s)
print(r3s)
print(rep)
print(e(rep))
print(r1s)
print(r2s)
print(r3s)
