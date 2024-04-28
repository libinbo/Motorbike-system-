
class Hund: # danner klassen hund

    def __init__(self,alder, vekt):# danner en konstruktør 
        self._alder=alder #lager instansvariablene alder, vekt, spis og metthet
        self._vekt=vekt 
        self._spis =0 # velger å sette den til å være null.slikt at det blir enklere legge til antallet
        self._metthet=10 # det blir oppgit i oppgaven at den skal alltid initaliserer med verdien10 
        
    def hent_alder(self): #lager en metode for å kunne hente alder 
        return self._alder # returner aldern 
    

    def hent_vekt(self): #lager en egen metode for å kunne hente vekten til hunden 
        
        return self._vekt #returnerer vekten til hunden 
    
    def spring(self): #lager en egen metode for at hunden skal "springe"
        if self._metthet <5: #hvis metthet er mindre 5 så skal den reduserer med 1, det samme gjelden vekten til hunden
            self._metthet -=1
            self._vekt -=1


    def spis (self,heltall): #lager en metode for at hunden skal kunne "spise", med parametern heltall

        if  self._metthet >7 : #hvis methett er mer en 7 så skal den legge på 1 på vekt og methhet 

            self._vekt+=1
            
            self._metthet+=1 

