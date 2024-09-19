ipt = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

r1s = [1,3,2,4,0]
r1b = [4,0,2,1,3]

r2s = [2,4,0,1,3]
r2b = [2,3,0,4,1]

r3s = [1,4,0,3,2]
r3b = [2,0,4,3,1]

minor=[2,3,0,1,4]

m=0

def enigma(a):
    
    pos = ipt.index(a)
    print(pos,"#notwrong")
    
    fin=r1s[pos]
    print(fin, "#1")
    
    fin=r2s[fin]
    print(fin, "#2")
    
    fin=r3s[fin]
    print(fin, "#3")

    
    fin=minor[fin]
    print(fin, "#4")
    
    fin=r3b[fin]
    print(fin, "#5")

    
    fin=r2b[fin]
    print(fin, "#6")

    
    fin=r1b[fin]
    print(fin, "#7")
    
    res = ipt[fin]
    
    #if r1s[0]==3 and r2s[0]==2:
    #    r1s.append(r1s.pop(0))
    #    r2s.append(r2s.pop(0))
    #    r3s.append(r3s.pop(0))
    #elif r1s[0]==3:
    #    r1s.append(r1s.pop(0))
    #    r2s.append(r2s.pop(0))
    #else:
    #    r1s.append(r1s.pop(0))

    return res
    
#turnr1=int(input())
#turnr2=int(input())
#turnr3=int(input())
rep = list(input())


#for i in range(0,turnr1):
#    r1s.append(r1s.pop(0))
#for i in range(0,turnr2):
#    r2s.append(r2s.pop(0))
#for i in range(0,turnr3):
#    r3s.append(r3s.pop(0))

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