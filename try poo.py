rep="texte" #uniquement lettre minuscule, caractère spéciaux autorisé : " " (oui que l'espace, rien d'autre)
repcopy=rep

class rouage:
    def __init__(self):
        self.turn1=0 #a remplacé,toute les valeur accepté au bout de 25 sa revient au meme
        self.turn2=0
        self.turn3=0

        self.rouage1="r1" #a remplacé de r1 a r5 inclue, pas deux fois le même
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
        self.ipt = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
         
    def turn(self,l1s,n):   #permet de simulé la rotation d'un rotor
        for i in range(n):
            l1s.append(l1s.pop(0))
            for i in range(len(l1s)):
                if l1s[i]==0:
                    l1s[i]=25
                else:
                    l1s[i]-=1
        return l1s
        
    def modif_list(self):    #permet de simulé le paramétrage des rotors
        for i in self.dico_rouage[self.rouage1]:
            i=self.turn(i,self.turn1)
        for i in self.dico_rouage[self.rouage2]:
            i=self.turn(i,self.turn2)        
        for i in self.dico_rouage[self.rouage3]:
            i=self.turn(i,self.turn3)
        return None
    
    def rotor(self,a):    #permet de simulé comment ce comporte une lettre a quand elle passe dans la série de rotor+fait tourné les rotors a la fin tout comme énigma
        pos = self.ipt.index(a)
        fin=self.dico_rouage[self.rouage1][0][pos]
        fin=self.dico_rouage[self.rouage2][0][fin]
        fin=self.dico_rouage[self.rouage3][0][fin]
        fin=self.minor[fin]
        fin=self.dico_rouage[self.rouage3][1][fin]
        fin=self.dico_rouage[self.rouage2][1][fin]
        fin=self.dico_rouage[self.rouage1][1][fin]
        res = self.ipt[fin]

        if self.dico_rouage[self.rouage2][0][0]== 1:
            for i in self.dico_rouage[self.rouage1]:
                i=self.turn(i,self.turn1)
            for i in self.dico_rouage[self.rouage2]:
                i=self.turn(i,self.turn2)        
            for i in self.dico_rouage[self.rouage3]:
                i=self.turn(i,self.turn3)
        elif self.dico_rouage[self.rouage1][0][0]== 1:
            for i in self.dico_rouage[self.rouage1]:
                i=self.turn(i,self.turn1)
            for i in self.dico_rouage[self.rouage2]:
                i=self.turn(i,self.turn2) 
        else:
            for i in self.dico_rouage[self.rouage1]:
                i=self.turn(i,self.turn1)

        return res    

class wire: 
    rouageh=rouage()
    def __init__(self):
        self.dicto={          #a remplacé,jamais deux fois la meme lettre et chaque liste doit etre complété
            '1d':["a","e"],
            '2d':["c","r"],
            '3d':["",""],
            '4d':["",""],
            '5d':["",""],
            '6d':["",""],
            '7d':["",""],
            '8d':["",""],
            '9d':["",""],
            '10d':["",""]
        }
        self.rep=rep

    def fil(self):   #permet de modifié les lettres de la phrase en fonction des cable au dessus
        self.rep = list(self.rep)
        for d in range(len(self.rep)):
            for i in self.dicto:
                if self.rep[d]==self.dicto[i][0]:
                    self.rep[d]=self.dicto[i][1]
                elif self.rep[d]==self.dicto[i][1]:
                    self.rep[d]=self.dicto[i][0]
                else:
                    None
        return self.rep

    def check(self):   #permet de vérifié si tout est respecté pour le bon fonctinnement
        temp=[]
        for i in self.dicto:
            for e in self.dicto[i]:
                temp.append(e)
        for i in temp:
            if temp.count(i) >1 and i !="":
                return False
        temp.clear()
        temp.append(rouageh.rouage1)
        temp.append(rouageh.rouage2)
        temp.append(rouageh.rouage3)
        for i in temp:
            if temp.count(i)>1 and (i=="" or " "):
                return False
        return True

class result:
    wireh=wire()
    rouageh=rouage()
    def __init__(self):
        self.ipt = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        return
    
    def resultat(self):   #permet de simulé le tout
        wireh.rep=wireh.fil()
        for i in range(len(wireh.rep)):
            if wireh.rep[i]==" ":
                pass
            else:
                wireh.rep[i]=rouageh.rotor(wireh.rep[i])
        wireh.rep=wireh.fil()
        return wireh.rep

#le finale, toute les fonctions sont mise ensemble pour avoir un texte a la sortie
rouageh=rouage()
wireh=wire()
resulth=result()

if __name__== "__main__" and wireh.check()==True:
    try:
        rouageh.modif_list()
        rep=resulth.resultat()
        print(repcopy,"; a été transformé en :",''.join(rep))
    except Exception as e:
        print(e)
else:
    print("il y a sans doute une erreur dans les paramétrage, vérifie bien que toute les règle sont respecté !")

