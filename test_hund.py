from hund import Hund

def hovedprogram(): #lager et hovedprogram 


    dog=Hund(14,12) #lager et objektet dog, som er 14 år og veier 12

    dog.spis(8) #objektet hund kaller på metoden spus med 8 som agrument 

    print(dog.hent_vekt()) #skriver ut veketen til hunden

    dog.spring() #hunden springer 

    print(dog.hent_vekt()) #skriver ut vekten til hunden 
    
    
    dog.spis(9) #objektet hund kaller på metoden spis med argumentet 9.
    
    print(dog.hent_vekt()) # henter vekt 

    dog.spring() # huden "springer" 

    print(dog.hent_vekt()) # henter vekten 
hovedprogram() #kaller på hovedprogrammet 