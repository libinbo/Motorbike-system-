from egen import Bok #fra filen egen importerer jeg klassen boka


def hovedprogram(): #lager prosedyren hovedprogram 

        Favbok1=Bok("Six of Crows", 2015, 100) # lager objekt favbok1, med boktitel. utgivelses år,og poeng jeg gir boka 

        Favbok2= Bok("The raven and the Dove",2020,95)#lager objektet favbok2, og med boktitelen the raven ande the dov, utgivelses åren en 2020, og antall poeng jeg gir er 85 

        Favbok3= Bok( "Instructions for Dancing",2021,90)# lager enda et objekt, med boktitel og år, og poeng 
    
        Favbok1.skriv_ut()# skriver objekt favbok1, ved å kalle på skriv_ut. Får ut titelen på boka, utgiver år, og poeng jeg har gitt boka 

        Favbok2.skriv_ut()# gjør det samme for favbok2

        Favbok3.skriv_ut()# og favbok3

hovedprogram() #til slutt kaller jeg bok hovedprogammet
