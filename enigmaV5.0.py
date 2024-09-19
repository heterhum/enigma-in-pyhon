ipt = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

r1s = [7, 19, 23, 1, 12, 16, 0, 24, 10, 4, 14, 21, 22, 9, 8, 18, 6, 3, 11, 25, 5, 15, 13, 17, 2, 20]
r1b = [6, 3, 24, 17, 9, 20, 16, 0, 14, 13, 8, 18, 4, 22, 10, 21, 5, 23, 15, 1, 25, 11, 12, 2, 7, 19]

r2s = [20, 8, 13, 24, 7, 14, 3, 9, 0, 22, 6, 4, 18, 11, 25, 10, 1, 19, 23, 5, 12, 21, 2, 16, 15, 17]
r2b = [8, 16, 22, 6, 11, 19, 10, 4, 1, 7, 15, 13, 20, 2, 5, 24, 23, 25, 12, 17, 0, 21, 9, 18, 3, 14]

r3s = [17, 6, 22, 10, 25, 14, 3, 21, 0, 13, 18, 2, 24, 11, 5, 23, 12, 9, 8, 16, 7, 4, 1, 19, 20, 15]
r3b = [8, 22, 11, 6, 21, 14, 1, 20, 18, 17, 3, 13, 16, 9, 5, 25, 19, 0, 10, 23, 24, 7, 2, 15, 12, 4]

minor=[2, 5, 0, 7, 4, 1, 9, 3, 11, 6, 13, 8, 15, 10, 17, 12, 19, 14, 21, 16, 23, 18, 24, 20, 22, 25]

m=0
rcop=[]

final = []
def turn(l1s,n):
    global rcop
    for i in range(0,n):
        l1s.append(l1s.pop(0))
        rcop=[]
        for i in l1s:
            if i==0:
                rcop.append(25)
            else:
                rcop.append(i-1)
    l1s=rcop
    return l1s
    
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
    #print(fin, "#7")
    res = ipt[fin]
    if r2s== 20:
        turn(r1s,1),turn(r1b,1)
        turn(r2s,1),turn(r2b,1)
        turn(r3s,1),turn(r3b,1)
    elif r1s == 7:
        turn(r1s,1),turn(r1b,1)
        turn(r2s,1),turn(r2b,1)
    else:
        turn(r1s,1),turn(r1b,1)
        
    return res

turn1=int(input())
turn2=int(input())
turn3=int(input())
rep = list(input())

r1s,r1b=turn(r1s,turn1),turn(r1b,turn1)
r2s,r2b=turn(r2s,turn2),turn(r2b,turn2)
r3s,r3b=turn(r3s,turn3),turn(r3b,turn3)

for i in rep:
    final.append(enigma(i))
  
print(final)