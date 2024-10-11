class rouage:
    def __init__(self):
        self.turn1=0
        self.turn2=0
        self.turn3=0 

        self.rouage1="r1"
        self.rouage2="r2"
        self.rouage3="r3"
        
        self.dico_rouage={
            "r1":[[7,19,23,1,12,16,0,24,10,4,14,21,22,9,8,18,6,3,11,25,5,15,13,17,2,20],[6,3,24,17,9,20,16,0,14,13,8,18,4,22,10,21,5,23,15,1,25,11,12,2,7,19]],
            "r2":[[20,8,13,24,7,14,3,9,0,22,6,4,18,11,25,10,1,19,23,5,12,21,2,16,15,17],[8,16,22,6,11,19,10,4,1,7,15,13,20,2,5,24,23,25,12,17,0,21,9,18,3,14]],   
            "r3":[[17,6,22,10,25,14,3,21,0,13,18,2,24,11,5,23,12,9,8,16,7,4,1,19,20,15],[8,22,11,6,21,14,1,20,18,17,3,13,16,9,5,25,19,0,10,23,24,7,2,15,12,4]],
            "r4":[[12,9,18,1,20,14,5,17,23,8,11,24,0,15,4,13,19,7,2,16,6,25,21,3,10,22],[12,3,18,23,14,6,20,17,9,1,24,10,0,15,5,13,19,7,2,16,4,22,25,8,11,21]],
            "r5":[[0,3,16,25,21,9,14,15,18,11,20,6,12,4,10,8,13,22,17,2,1,23,24,5,7,19],[0,20,19,1,13,23,11,24,15,5,14,9,12,16,6,7,2,18,8,25,10,4,17,21,22,3]]
            
        }
        
        self.minor = [2,5,0,7,4,1,9,3,11,6,13,8,15,10,17,12,19,14,21,16,23,18,24,20,22,25]
        
    def turn(self,l1s,n):
        for i in range(n):
            l1s.append(l1s.pop(0))
            for i in range(len(l1s)):
                if l1s[i]==0:
                    l1s[i]=4
                else:
                    l1s[i]-=1
        return l1s
        
    def modif_list(self):
        for i in self.dico_rouage[self.rouage1]:
            i=self.turn(i,self.turn1)
        for i in self.dico_rouage[self.rouage2]:
            i=self.turn(i,self.turn2)        
        for i in self.dico_rouage[self.rouage3]:
            i=self.turn(i,self.turn3)
        return None
            
class wire: #to do, optimisé comment les file sont géré
class res: #to do, avoir une fonction qui nous affiche le résultat finale
