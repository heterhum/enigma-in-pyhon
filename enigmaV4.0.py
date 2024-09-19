ipt = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

r1s = [7, 19, 23, 1, 12, 16, 0, 24, 10, 4, 14, 21, 22, 9, 8, 18, 6, 3, 11, 25, 5, 15, 13, 17, 2, 20]
r1b = [6, 3, 24, 17, 9, 20, 16, 0, 14, 13, 8, 18, 4, 22, 10, 21, 5, 23, 15, 1, 25, 11, 12, 2, 7, 19]

r2s = [20, 8, 13, 24, 7, 14, 3, 9, 0, 22, 6, 4, 18, 11, 25, 10, 1, 19, 23, 5, 12, 21, 2, 16, 15, 17]
r2b = [8, 16, 22, 6, 11, 19, 10, 4, 1, 7, 15, 13, 20, 2, 5, 24, 23, 25, 12, 17, 0, 21, 9, 18, 3, 14]

r3s = [17, 6, 22, 10, 25, 14, 3, 21, 0, 13, 18, 2, 24, 11, 5, 23, 12, 9, 8, 16, 7, 4, 1, 19, 20, 15]
r3b = [8, 22, 11, 6, 21, 14, 1, 20, 18, 17, 3, 13, 16, 9, 5, 25, 19, 0, 10, 23, 24, 7, 2, 15, 12, 4]

minor=[2, 5, 0, 7, 4, 1, 9, 3, 11, 6, 13, 8, 15, 10, 17, 12, 19, 14, 21, 16, 23, 18, 24, 20, 22, 25]

m=0

final = []

def enigma(a):
    
    pos = ipt.index(a)
    #print(pos,"#notwrong")
    
    fin=r1s[pos]
    #print(fin, "#1")
    
    fin=r2s[fin]
    #print(fin, "#2")
    
    fin=r3s[fin]
    #print(fin, "#3")

    fin=minor[fin]
    #print(fin, "#4")
    
    fin=r3b[fin]
    #print(fin, "#5")
    
    fin=r2b[fin]
    #print(fin, "#6")

    fin=r1b[fin]
    fin=r1s[fin]
    fin=r1s.index(fin)
    #print(fin, "#7")
    
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
    final.append(enigma(i))
  
print(final)







