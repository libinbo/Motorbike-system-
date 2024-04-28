class Motorsykkel: #lager klassen Motorsykkel 

    def __init__(self,merke, regnum): #danner en konstruør  med 
        self._regnum=regnum # danner de tre instansvariablene, regnumer, merke og km. Km inasialiserer altid til å være 0.
        self._merke= merke 
        self._km =0

    def kjør(self,km): # danner metoden kjør 
        self._km+=km # instansvariabelen self.km legger til km 
    

    def hent_kilmoeteravstand(self):  #en metode brukt for å hente kilmentern 
        
        return self._km # returnerer kilometern

    def skriv_ut(self): # lager en metode som skriver ut merke,regnumer og antall km motorsykelen kjører.

         print("merke mitt er:", self._merke)

         print("regristeringsnummer mitt er:", self._regnum)

         print("antall avstand den kjører er første gang :", self._km)

    




