turn1=0 #put the number of gear rotation here
turn2=0#put the number of gear rotation here
turn3=0 #put the number of gear rotation here

class rouage:
    def __init__(self):
        self.r1s = [7,19,23,1,12,16,0,24,10,4,14,21,22,9,8,18,6,3,11,25,5,15,13,17,2,20]
        self.r1b = [6,3,24,17,9,20,16,0,14,13,8,18,4,22,10,21,5,23,15,1,25,11,12,2,7,19]
        
        self.r2s = [20,8,13,24,7,14,3,9,0,22,6,4,18,11,25,10,1,19,23,5,12,21,2,16,15,17]
        self.r2b = [8,16,22,6,11,19,10,4,1,7,15,13,20,2,5,24,23,25,12,17,0,21,9,18,3,14]
        
        self.r3s = [17,6,22,10,25,14,3,21,0,13,18,2,24,11,5,23,12,9,8,16,7,4,1,19,20,15]
        self.r3b = [8,22,11,6,21,14,1,20,18,17,3,13,16,9,5,25,19,0,10,23,24,7,2,15,12,4]
        
        self.r4s = [12,9,18,1,20,14,5,17,23,8,11,24,0,15,4,13,19,7,2,16,6,25,21,3,10,22]
        self.r4b = [12,3,18,23,14,6,20,17,9,1,24,10,0,15,5,13,19,7,2,16,4,22,25,8,11,21]
        
        self.r5s = [0,3,16,25,21,9,14,15,18,11,20,6,12,4,10,8,13,22,17,2,1,23,24,5,7,19]
        self.r5b = [0,20,19,1,13,23,11,24,15,5,14,9,12,16,6,7,2,18,8,25,10,4,17,21,22,3]
        {
            "r1"=[r1s,r1b]
        }
        
        self.minor = [2,5,0,7,4,1,9,3,11,6,13,8,15,10,17,12,19,14,21,16,23,18,24,20,22,25]
        
    def turn(self,l1s,n):
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
        
main.rouage()
temp=main.__dict__
choix1,choix1b=temp[r1s],temp[r1b]
choix2,choix2b=temp[r2s],temp[r2b]
choix3,choix3b=temp[r3s],temp[r3b]

main.turn()

main.turn()