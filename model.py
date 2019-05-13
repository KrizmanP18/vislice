stevilo_dovoljenih_napak =10
pravilna_crka ='+'
ponovljena_crka ='0'
napacna_crka ='-'
zmaga ='W'
poraz ='X'

class Igra:
    def __init__(self,geslo,crke):
        self.geslo = geslo
        self.crke = crke

    def napacne_crke(self):
        seznam = []
        for crka in self.crka:
           if crka not in self.geslo:
               seznam.append(crka)
        return seznam       

        
    def pravilne_crke(self):
        seznam = []
        for crka in self.crka:
           if crka in self.geslo:
               seznam.append(crka)
        return seznam       
        

    def stevilo_napak(self):
       return len(napacne_crke)

    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.crka:
            return False
        return True
           
    def poraz(self):
        for crka in self.geslo:
            if crka in self.crka:
            return False
        return True    

    def pravilni_del_gesla(self):
        niz = ''
       for crka in self.geslo:
           if crka in self.crke:
            niz += crka = ''
        else: 
            niz += '_'  
            return niz   

    def nepravilni_ugibi(self):
        niz = ''
        for crka in self.geslo:
            if crka not in self.crke:
                niz += ''
    return niz


    def ugibaj(self):               


