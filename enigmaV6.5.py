#do not touch this group of variable
ipt = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
r1s = [7,19,23,1,12,16,0,24,10,4,14,21,22,9,8,18,6,3,11,25,5,15,13,17,2,20]
r1b = [6,3,24,17,9,20,16,0,14,13,8,18,4,22,10,21,5,23,15,1,25,11,12,2,7,19]
r2s = [20,8,13,24,7,14,3,9,0,22,6,4,18,11,25,10,1,19,23,5,12,21,2,16,15,17]
r2b = [8,16,22,6,11,19,10,4,1,7,15,13,20,2,5,24,23,25,12,17,0,21,9,18,3,14]
r3s = [17,6,22,10,25,14,3,21,0,13,18,2,24,11,5,23,12,9,8,16,7,4,1,19,20,15]
r3b = [8,22,11,6,21,14,1,20,18,17,3,13,16,9,5,25,19,0,10,23,24,7,2,15,12,4]
r4s = [12,9,18,1,20,14,5,17,23,8,11,24,0,15,4,13,19,7,2,16,6,25,21,3,10,22]
r4b = [12,3,18,23,14,6,20,17,9,1,24,10,0,15,5,13,19,7,2,16,4,22,25,8,11,21]
r5s = [0,3,16,25,21,9,14,15,18,11,20,6,12,4,10,8,13,22,17,2,1,23,24,5,7,19]
r5b = [0,20,19,1,13,23,11,24,15,5,14,9,12,16,6,7,2,18,8,25,10,4,17,21,22,3]
minor = [2,5,0,7,4,1,9,3,11,6,13,8,15,10,17,12,19,14,21,16,23,18,24,20,22,25]
m=0
rcop=[]
final = []

turn1=0 #put the number of gear rotation here
turn2=0 #put the number of gear rotation here
turn3=0 #put the number of gear rotation here
rep = list(input())

#do not use the same gear
rotor1s,rotor1b=r1s,r1b #put the number of gear that you wanna use
rotor2s,rotor2b=r2s,r2b #put the number of gear that you wanna use
rotor3s,rotor3b=r3s,r3b #put the number of gear that you wanna use

#put the wire here f0,f0b="-","_"|f0!=f0b|if you only want a certain number of wire, fill with None
f1,f1b=None,None
f2,f2b=None,None
f3,f3b=None,None
f4,f4b=None,None
f5,f5b=None,None
f6,f6b=None,None
f7,f7b=None,None
f8,f8b=None,None
f9,f9b=None,None
f10,f10b=None,None

#do not touch this variable
checklist = [f1, f1b, f2, f2b, f3, f3b, f4, f4b, f5, f5b, f6, f6b, f7, f7b, f8, f8b, f9, f9b, f10, f10b]

#simule the rotation of gear            
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
    
#simule the gear
def rotor(a):
    global rotor1s,rotor1b,rotor2s,rotor2b,rotor3s,rotor3b
    pos = ipt.index(a)
    fin=rotor1s[pos]
    fin=rotor2s[fin]
    fin=rotor3s[fin]
    fin=minor[fin]
    fin=rotor3b[fin]
    fin=rotor2b[fin]
    fin=rotor1b[fin]
    res = ipt[fin]
    
    if r2s== 20:
        rotor1s,rotor1b=turn(rotor1s,1),turn(rotor1b,1)
        rotor2s,rotor2b=turn(rotor2s,1),turn(rotor2b,1)
        rotor3s,rotor3b=turn(rotor3s,1),turn(rotor3b,1)
    elif r1s == 7:
        rotor1s,rotor1b=turn(rotor1s,1),turn(rotor1b,1)
        rotor2s,rotor2b=turn(rotor2s,1),turn(rotor2b,1)
    else:
        rotor1s,rotor1b=turn(rotor1s,1),turn(rotor1b,1)
        
    return res
    
#simule wire on enigma
def fil(tf1,tf2,i):
    if i == tf1:
        i=tf2
        return i
    elif i == tf2:
        i=tf1
        return i
    else:
        return i
    
#check if the same letter is in 2+ wire
def check():
    for i in checklist:
        if checklist.count(i) >1 and i !=None:
            print("erreur:",i,"est présent",checklist.count(i),"fois")
            exit()

#put everything together
def resultat():
    for i in rep:
        fil(f1,f1b,i)
        fil(f2,f2b,i)
        fil(f3,f3b,i)
        fil(f4,f4b,i)
        fil(f5,f5b,i)
        fil(f6,f6b,i)
        fil(f7,f7b,i)
        fil(f8,f8b,i)
        fil(f9,f9b,i)
        fil(f10,f10b,i)
        i=rotor(i)
        fil(f1,f1b,i)
        fil(f2,f2b,i)
        fil(f3,f3b,i)
        fil(f4,f4b,i)
        fil(f5,f5b,i)
        fil(f6,f6b,i)
        fil(f7,f7b,i)
        fil(f8,f8b,i)
        fil(f9,f9b,i)
        fil(f10,f10b,i)
        final.append(i)
    return final

check()

r1s,r1b=turn(r1s,turn1),turn(r1b,turn1)
r2s,r2b=turn(r2s,turn2),turn(r2b,turn2)
r3s,r3b=turn(r3s,turn3),turn(r3b,turn3)

print(resultat())