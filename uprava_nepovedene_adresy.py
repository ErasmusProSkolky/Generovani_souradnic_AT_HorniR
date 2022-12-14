# otevření souboru, z něhož bereme souřadnice
with open('AT_adresy_gpsvizualizer.csv', encoding='utf-8') as vstup:
    radky = vstup.readlines()

# uložení souřadnic do proměnných
udaje = [udaj.split(";") for udaj in radky]
latitude = [udaj[0] for udaj in udaje[1:]]
longitude = [udaj[1] for udaj in udaje[1:]]

# otevření souboru, do kterého budeme souřadnice ukládat vždy na konec řádku
with open('AT_nepovedene_MS.csv', encoding='utf-8') as soubor:
     obsah = soubor.readlines()

radek = [radek.split('\n') for radek in obsah]
radek = [udaj[0] for udaj in radek]

# uložení souřadnic na konec řádku
cislo_radku = 0
skolky = []
for r in radek:
    skolka = radek[cislo_radku] + latitude[cislo_radku] + ';' + longitude[cislo_radku] + '\n'
    skolky.append(skolka)
    cislo_radku+=1

# vložení nových řádků do souboru k ostatním skolkam
with open('AT_souradnice_MS.csv', mode='a', encoding='utf-8') as vystup:
    vystup.writelines(skolky)

