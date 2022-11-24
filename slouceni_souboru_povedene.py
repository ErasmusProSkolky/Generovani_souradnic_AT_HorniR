# otevření souboru Freistadt
with open('AT_povedene_Freistadt.csv', encoding='utf-8') as vstup:
    Freistadt = vstup.readlines()

# otevření souboru Rohrbach
with open('AT_povedene_Rohrbach.csv', encoding='utf-8') as vstup:
    Rohrbach = vstup.readlines()

# otevření souboru Uhrfahr
with open('AT_povedene_Urfahr.csv', encoding='utf-8') as vstup:
    Urfahr = vstup.readlines()

vse = Freistadt + Rohrbach[1:] + Urfahr[1:]

# uložení do souboru
with open('AT_souradnice_MS.csv', mode='w', encoding='utf-8') as vystup:
    vystup.writelines(vse)