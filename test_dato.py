from dato import Dato  # fra filen dato importer jeg klassen Dato.


def hovedprogram(): #deffinerer et hovedprogram

    dato1= Dato(14,2,1999) #lager objektet dato1 fra klassen dato, med 14 som dato, 2, som måned og 1999 som år.

    print(dato1.hent_aar()) #skriver ut datoes år 

    #lager if setningen, hvis dato1 har 15 som dato, så skriver det ut lønnigsdag.
    
    if dato1.bestemtdag(15): 
        
        print("Loenningsdag")

    elif dato1.bestemtdag(1) : #og hvis dato1 har 1 som dato så skrives det ut ny måande, nye muligheter

        print("Ny maande, nye muligheter")
    
    
    print(dato1.datostreng()) #printer ut dato, månde og år som en lesbar streng.

hovedprogram() #kaller på hovedprogrammet.


