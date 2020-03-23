import random


class Mitarbeiter:
    class_counter=1
    def __init__(self , Name):

        self.Name = Name.title()
        self.id = Mitarbeiter.class_counter
        class_counter=+1

    def __str__(self):
        return "Name: {}, Personalid {}:".format(self.Name, self.id)

    def GetPersonalID(self):
        return self.id





class Angestellter(Mitarbeiter):

    def __str__(self):
        return Mitarbeiter.__str__(self) +", Jahresgehalt : " + str(self.mon_gehalt*12)

    def SetGehalt  (self,mon_gehalt):
         self.mon_gehalt = mon_gehalt
         self.Jahresgehalt = mon_gehalt*12
         return self.Jahresgehalt

    def GetGehalt (self):
         #self.mon_gehalt = mon_gehalt

         return self.mon_gehalt
    def CalcSteuer(self):
        if self.Jahresgehalt <= 20000:
            return self.Jahresgehalt*20/100
        elif 20000<self.Jahresgehalt<=50000:
            return self.Jahresgehalt * 30 / 100
        elif self.Jahresgehalt >= 50000:
            return self.Jahresgehalt*40/100
        else:
            return "Fehler"



class Manager(Angestellter):
    Arbeiterliste = []
    def __str__(self):
        return Mitarbeiter.__str__(self) + ", Jahresgehalt : " + str(self.mon_gehalt * 12) + "Bonus" + str(self.bonus) + "mitarbeiter" + self.mitarbeiter
    def SetGehalt  (self,mon_gehalt,bonus):
         self.bonus = bonus
         self.mon_gehalt = mon_gehalt
         self.Jahresgehalt = mon_gehalt*12
         return self.Jahresgehalt ,bonus

    def GetGehalt (self):
         #self.mon_gehalt = mon_gehalt

         return self.mon_gehalt + self.bonus
    def AddArbeiter (self, Arbeiter):
        self.Arbeiter = Angestellter.__str__()
        Arbeiterliste = []

        Arbeiterliste.append(self.Arbeiter)

alex = Angestellter ("Krischna Alexander Jefferson").SetGehalt (3500)
emil = Manager ("emil tischbein").SetGehalt (5000, 1000)
emil.AddArbeiter (alex)

print (emil)




