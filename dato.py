

class Dato: #lager klassen dato 

    def __init__(self,ny_dag,ny_maande,ny_aar): #danner en konstruktør, med 
        
        self._ny_dag= ny_dag # konstruktøren har diee tre instansvariablene, nydag, nymaande, ny år

        self._ny_maande=ny_maande

        self._ny_aar=ny_aar


        self._bestemtdag=0 # lager en instansvaribaelen bestemtdag med verdien 0, slikt at den starter på 0.

    
    def hent_aar(self): # funksjunmetode for å hente år 

         return self._ny_aar  # retunerer år




    def datostreng(self): # funksjunsmetode for å sette dato, månde og år til en tekst streng
        
        datostreng="Datoen din er "+  str (self._ny_dag)+ str(self._ny_maande)+ str(self._ny_aar)

    
        return datostreng


    def bestemtdag(self,bestemtdag): # funskunsmetoden bestemtdag 
        
        if self._ny_dag == bestemtdag: # hvis datoen vår er lik bestemt dato så kommer det opp true på terminalen

            return True 

       
        else:
            return False # hvis ikke kommer det opp false på terminalen
