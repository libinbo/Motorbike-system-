
from motorsykkel import Motorsykkel

def hovedprogram():
    ms1=Motorsykkel("BMW", 1314) #lager objekt ms1 med BMW som merke, og 1314 som regnumer 
    ms2=Motorsykkel("volvo", 3009) #lager objekt ms2 med volovo som merke og 3009 som regnumer
    ms3=Motorsykkel("Harley", 1402) #lager objekt3 ms3 med merket harley og 1402 som regnumer
    
    ms3.kjør(10) #objekt ms3 med metoden kjør har 10 som argument, altså den kjører 10 km

    ms1.skriv_ut() #informasjon om regnumer, avstand, og merke blir skrvet ut for ms1 
    ms2.skriv_ut() # det samme skjer for ms2 og ms3
    ms3.skriv_ut()


hovedprogram()  #kaller på hovedprogrammet.
