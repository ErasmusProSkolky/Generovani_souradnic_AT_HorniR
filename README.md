Generování souřadnic (zvlášť pro každou ze 3 oblastí)
    
    soubor: souradnice_skolky_AT_Urfahr.py
    
    vstup: adresy_rakouske_ms_Urfahr_Umgebung.csv
    
    výstup: AT_povedene_Urfahr.csv, AT_nepovedene_Urfahr.csv



    soubor: souradnice_skolky_AT_Freistadt.py
    
    vstup: adresy_rakouske_ms_Freistadt.csv
    
    výstup: AT_povedene_Freistadt.csv, AT_nepovedene_Freistadt.csv


    soubor: souradnice_skolky_AT_Rohrbach.py

    vstup: adresy_rakouske_ms_Rohrbach.csv

    výstup: AT_povedene_Rohrbach.csv, AT_nepovedene_Rohrbach.csv
		
Sloučení povedených

    soubor: slouceni_souboru_povedene.py
    
    vstup: AT_povedene_Urfahr.csv, AT_povedene_Freistadt.csv, AT_povedene_Rohrbach.csv
    
    výstup: AT_souradnice_MS.csv
		
Sloučení nepovedených

    soubor: slouceni_souboru_nepovedene.py
    
    vstup: AT_nepovedene_Urfahr.csv, AT_nepovedene_Freistadt.csv, AT_nepovedene_Rohrbach.csv
    
    výstup: AT_nepovedene_MS.csv 

Extrakce souřadnic ze soubou vygenerovaného Gpsvizualizer, uložení souřadnic do jednotlivých řádků v AT_nepovedene_MS.csv a následné uložení původně nepovedených adres do  AT_souradnice_MS.csv
    
    soubor: uprava_nepovedene_adresy.py

    vstup: AT_adresy_gpsvizualizer.csv, AT_nepovedene_MS.csv

    výstup: AT_souradnice_MS.csv - obohacený o nové řádky
