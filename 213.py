#class Person:

#    def __init__(self, imie, wiek):  
 #       self.imie = imie
 #       self. wiek = wiek

 #   def witam(self):
 #       print("witam jestem wesoły " + self.imie + " mam " + str(self.wiek) + " lat")
    
#p1 = Person('Luki', 18)

#print(p1.imie)
#p1.witam()


#--------------------------------------------------

#import datetime

#class drewno:

#    def __init__(self, imie, data):
#        self.imie=imie
#        self.data=data
    
#    def character(self):
#        timez=datetime.datetime.now()
#        timez=timez.year
#        print(self.imie + " masz " + str(timez - self.data) + " lat ")

#osoba1=drewno('Lukson',2002)
#osoba1.character()

#---------------------------------------------------
import random as rd
class losowanie:
    def __init__(self):
        self.nazwa=2

    def loso(self):
        self.nazwa=rd.randrange(0,2)
        return self.nazwa

    def porownanie(self,x):
        self.loso()
        if x==self.nazwa:
            print("zgadles")
        else:
            print("unlucky")

tak=losowanie()
wpisznr=int(input("wybierz 0-1 "))
tak.porownanie(wpisznr)

