class Bok: #lager kalssen bok. 


    def __init__(self,titel,år,poeng): # danner en konstrøer

        self._titel=titel  #insatnsvaribalene, titiel, år og poeng 

        self._år=år

        self._poeng=poeng

    def titel(self): #lager en metoden titel 
        
        return self._titel # hoved funkjunen er å kunne returne titelen til boka 

    def år(self): # lage metoden år 

      return self._år #returnerer utgivelses år 
    
    def poeng(self):# lager en ny metode som hetter poeng 

       return self._poeng #returnerer poeng for boka 



    def skriv_ut(self): # ny metode som kalles for skriv ut 

        print("Titelen på boka er:", self._titel) #skriver ut titelen for boka 

        print("Utgivelsesår for boka er:",  self._år) #skriver ut utgivelses år for boka 

        print("poeng jeg gir boka er: ",self._poeng)#skriver ut poeng for boka 