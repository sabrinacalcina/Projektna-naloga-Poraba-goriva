import os
import random, json

STANJE ='stanje.txt'

class Model:

    def __init__(self):
        self.seznam = []
        self.osvezi_seznam()

    def vnesi_tank(self,podatki):
        # zapise vnesene podatke v datoteko
        podatki = '{}, {}, {}, {}\n'.format(podatki.get('datum'), podatki.get('tank'), podatki.get('stanje'), podatki.get('cena'))
        with open(STANJE, 'a') as datoteka:
            datoteka.write(podatki)
        self.seznam.append(podatki)

    def razveljavi(self):
        # izbrise zadnji vnos
        if os.stat(STANJE).st_size != 0:
            self.seznam = self.seznam[:-1]
            lines = self.seznam
            with open(STANJE,'w') as zgodovina:
                zgodovina.writelines([item for item in lines])

    def km_tankamo(self):
        stanje_stevca = []
        for element in self.seznam:
            stanje_stevca.append(float(element.split(',')[2]))
        n = len(stanje_stevca)
        vsota = 0
        for i in range(0, n-1):
            vsota += (stanje_stevca[i + 1] - stanje_stevca[i])
    
        if n > 1:
            return  round(vsota / (n - 1) , 3) 
        else:
            return 0

    def cena(self):
        if len(self.seznam) <= 1:
            return 0
        else:
            s = self.seznam[-1]
            p = self.seznam[-2]
            zadnja_cena = float(s.split(',')[3])
            predzadnja_cena = float(p.split(',')[3])
            return round(zadnja_cena - predzadnja_cena,3)

    def poraba_avta(self):
        if len(self.seznam) <= 1:
            return 0
        else:
            v = self.seznam[-1]
            z = self.seznam[0]
            prvo_stanje = float(z.split(',')[2])
            zadnje_stanje = float(v.split(',')[2])
        
            tank = 0
            m = len(self.seznam)
            for e in self.seznam[:m - 1]:
                tank += float(e.split(',')[1])
            return round(tank * 100 / (zadnje_stanje - prvo_stanje), 3)
        
    def osvezi_seznam(self):
        self.seznam = []
        try:
            if os.stat(STANJE).st_size != 0:
                with open(STANJE) as zgodovina:
                    for vrstica in zgodovina:
                        self.seznam.append(vrstica)
        except:
            f = open(STANJE, "w+")
            print('Ustvarjena nova datoteka')
            f.close()

    def litri(self):
        tank = []
        for e in self.seznam:
            tank.append(float(e.split(',')[1]))
        return tank

    def reset_funkcija(self):
        if os.path.exists(STANJE):
            os.remove(STANJE)
            self.seznam = []
        else:
            print('Datoteka ne obstaja.')

    def prikazi_zgodovino(self): 
        # osvezimo prikaz
        zgo = self.seznam[-5:]
        if len(zgo) < 5:
            zgo = [', , , ',', , , ',', , , ',', , , ',', , , '] + zgo
        return zgo
  
    def izracun_stroskov(self, podatki):
        razdalja = float(podatki.get('razdalja'))
        poraba = float(podatki.get('poraba'))
        cena = float(podatki.get('cena'))
        return razdalja * poraba * cena / 100
        
        




