ipt = ['a', 'b', 'c', 'd']#, 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

r1s = [3,1,0,2]
r2s = [2,3,0,1]
r3s = [0,3,1,2]
minor=[1,0,2,3]

def e(a):
    pos = ipt.index(a)
    print(pos,"#1")
    
    for index, listes in enumerate(r1s):
        print(index,listes)
        if index == pos:
            fin = listes
    print(fin,"#2")
    
    for index, listes in enumerate(r2s):
        print(index,listes)
        if index == fin:
            fin = listes
    print(fin,"#3")
    
    for index, listes in enumerate(r3s):
        print(index,listes)
        if index == fin:
            fin = listes
    print(fin,"#4")
    
    for index, listes in enumerate(minor):
        print(index,listes)
        if index == fin:
            fin = listes
    print(fin,"#5")
    
    for index, listes in enumerate(r3s):
        print(index,listes)
        if index == fin:
            fin = listes
    print(fin,"#6")
    
    for index, listes in enumerate(r2s):
        print(index,listes)
        if index == fin:
            fin = listes
    print(fin,"#7")
    
    for index, listes in enumerate(r1s):
        print(index,listes)
        if index == fin:
            fin = listes
    print(fin,"#8")
    
    res = ipt[fin]
    return res

print(e(input()))




#liste.append(liste.pop(0))
#print(liste)
#for index, listes in enumerate(liste, start=1):
#    print(index, listes)
    
