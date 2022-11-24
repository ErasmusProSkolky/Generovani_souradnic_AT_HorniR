# import modulu geopy
from geopy.geocoders import Nominatim
 
# načtení the Nominatim tool
loc = Nominatim(user_agent="GetLoc")

# otevření souboru 1
with open('adresy_rakouske_ms_Rohrbach.csv', encoding='utf-8') as vstup:
    radky = vstup.readlines()

# uložení neprázdných řádků do proměnné
skolky = []
for radek in radky:
    if radek != ";;;\n":
        skolky.append(radek)

# vytvoření seznamu z jednoho řádku
jeden_radek = [radek.split('\n') for radek in skolky]

# proměnné pro ukládání 
nepovedene = []
povedene = []

# generování souřadnic - povedené se ukládají do jednoho souboru a nepovedené do jiného
for cast_radku in jeden_radek[1:]:
    try:
        # rozdělení řádku na jednotlivé údaje
        cast = cast_radku[0].split(";")
                
        # načtení adresy ze zdrojové tabulky
        getLoc = loc.geocode(cast[1] + ',' + cast[3])
 
        # vypsání adresy a souřadnic (pro kontrolu)
        print(getLoc.address)
        print("Latitude = ", getLoc.latitude, "\n")
        print("Longitude = ", getLoc.longitude)
        
        # uložení povedených adres a dalších údajů do proměnné povedene
        skolka = ""
        for c in cast:
            skolka+= c + ";"
        povedene.append(skolka + str(getLoc.latitude) + ";" + str(getLoc.longitude) + "\n")
    except Exception as chyba:
        # uložení údajů do proměnné nepovedene
        data = ""
        for casti in cast:
            data+=casti+";"    
        nepovedene.append(data+"\n")
        print(chyba)
        pass

# vložení hlavičky u povedených
hlavicka = "NAZEV" + ";" + "ULICE" + ";" + "ZIP_CODE" + ";" + "MESTO" + ";" + "LATITUDE" + ";" + "LONGITUDE" + "\n"
povedene.insert(0,hlavicka)
# print(povedene)

# uložení povedených a nepovedených do souboru
with open("AT_povedene_Rohrbach.csv", "w", encoding="utf-8") as vystup:
    vystup.writelines(povedene)

with open("AT_nepovedene_Rohrbach.csv", "w", encoding="utf-8") as soubor:
    soubor.writelines(nepovedene) 