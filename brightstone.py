import os

order_lijst=[]

# Kop teksten :
SCR_TITLE = "BRIGHTSTONE ORDERS - DAGOVERZICHT"
OMZET_TITLE = "TOTALE OMZET"
DUURSTE_PRODUCT_TITLE = "DUURSTE PRODUCT"
AANTAL_ORDERS_TITLE = "AANTAL ORDERS"

TITLE_PRODUCT_NAAM = "Product Naam"
TITLE_KLANT = "Klant"
TITLE_AANTAL = "Aantal"
TITLE_PRIJS = "Prijs"

#voor table sjabloon
MENU_TEKSTEN_PLEK = "---MENUTEXTENPLEK---"
MENU_PLEK = "---MENUPLEK---\n"
RESULTAAT_TEKSTEN_PLEK = "---RESULTAATTEKSTENPLEK---\n"
RESULTAAT_PLEK = "---RESULTAATPLEK---\n"
WAARSCHUWING_TEKSTEN_PLEK = "---WAARSCHUWINGTEKSTENPLEK---\n"
WAARSCHUWING_PLEK = "---WAARSCHUWINGPLEK---\n"


SCR_BREEDTE = 85 #hoofd table breedte
COLUMN_PRODUCT_NAAM_BREEDTE = 30 #toon alle producten columns
COLUMN_KLANT_BREEDTE = 30        #toon alle producten columns
COLUMN_AANTAL_BREEDTE = 10       #toon alle producten columns
COLUMN_PRIJS_BREEDTE = 10        #toon alle producten columns


def main():
    #maak een lege table met menu
    hoofdscherm_sjablon_scr = maak_hoofdscherm()
    lege_tekst = voorbereid_bericht(" ")
    hoofdscherm_sjablon_scr = toevoeg_inhoud_aanhoofdscherm(hoofdscherm_sjablon_scr, lege_tekst)
    hoofdscherm_sjablon_scr = toevoeg_waarschuwing_aanhoofdscherm(hoofdscherm_sjablon_scr, lege_tekst)
    print(hoofdscherm_sjablon_scr)

    #Ik maak het scherm leeg en bereid het menu voor.
    keuze=""
    waarschuwing_tekst=""

    #Ik gebruik een while-lus om het programma te laten draaien totdat alle 5 opties zijn geselecteerd.
    while True:
        try:
            keuze = input("Maak een keuze [1-5]: ")
            keuze_integer = int(keuze)  #Ik voer een controle uit door de ingevoerde waarde
                                        # naar een geheel getal om te zetten.
                                        # Als er een fout is, vang ik die op.
                                        # Dan realiseer ik me dat het geen geheel getal is.


            if keuze_integer == 1:
                toon_alle_orders()
            elif keuze_integer == 2:
                bereken_totale_omzet()
            elif keuze_integer == 3:
                aantal_orders()
            elif keuze_integer == 4:
                toon_duurste_product()
            elif keuze_integer == 5:
                break
            elif keuze_integer < 1 or keuze_integer > 5: #Ik controleer of de ingevoerde waarde tussen 1 en 5 ligt.
                #teken de sjabloon
                hoofdscherm_sjablon_scr = maak_hoofdscherm()
                lege_tekst = voorbereid_bericht(" ")
                hoofdscherm_sjablon_scr = toevoeg_inhoud_aanhoofdscherm(hoofdscherm_sjablon_scr, lege_tekst)
                waarschuwing_tekst = (f"Jouw keuze moet tussen 1 en 5 liggen. Maar '{keuze_integer}' is geen optie.")
                hoofdscherm_sjablon_scr = toevoeg_waarschuwing_aanhoofdscherm(hoofdscherm_sjablon_scr,voorbereid_bericht(waarschuwing_tekst))
                print(hoofdscherm_sjablon_scr)
        except ValueError as e:
            #teken de sjabloon
            hoofdscherm_sjablon_scr = maak_hoofdscherm()
            lege_tekst = voorbereid_bericht(" ")
            hoofdscherm_sjablon_scr = toevoeg_inhoud_aanhoofdscherm(hoofdscherm_sjablon_scr, lege_tekst)
            waarschuwing_tekst = f"'{keuze}' is geen nummer."
            hoofdscherm_sjablon_scr = toevoeg_waarschuwing_aanhoofdscherm(hoofdscherm_sjablon_scr,
                                                                          voorbereid_bericht(waarschuwing_tekst))
            print(hoofdscherm_sjablon_scr)
        except TypeError as e:
            # teken de sjabloon
            hoofdscherm_sjablon_scr = maak_hoofdscherm()
            lege_tekst = voorbereid_bericht(" ")
            hoofdscherm_sjablon_scr = toevoeg_inhoud_aanhoofdscherm(hoofdscherm_sjablon_scr, lege_tekst)
            waarschuwing_tekst = (f"Controleer de gegevens. Een van prijs is geen nummer.")
            hoofdscherm_sjablon_scr = toevoeg_waarschuwing_aanhoofdscherm(hoofdscherm_sjablon_scr,
                                                                          voorbereid_bericht(waarschuwing_tekst))
            print(hoofdscherm_sjablon_scr)


# schone terminal
def schone_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def maak_hoofdscherm():
    schone_terminal() # schone de terminal
    scr = toevoeg_menu_aanhoofdscherm(hoofdschrem_sjablon(), maak_menu_lijst()) #voeg menu aan het hoofdscherm toe.
    return scr #teken hoofd scherm



def hoofdschrem_sjablon():
    #dit is de sjabloon van het hoofdscherm
    horizontal_line = "\u2501"
    scr_frame = ""
    # top line
    scr_frame += f"\u250F{horizontal_line * SCR_BREEDTE}\u2513\n"
    scr_frame += f"\u2503\033[32m\033[44m\033[1m" + SCR_TITLE.center(SCR_BREEDTE) + "\033[0m\u2503\n"
    scr_frame += f"\u2523{horizontal_line * SCR_BREEDTE}\u2528\n"
    scr_frame += MENU_PLEK
    scr_frame += f"\u2523{horizontal_line * SCR_BREEDTE}\u2528\n"
    scr_frame += RESULTAAT_PLEK
    scr_frame += f"\u2523{horizontal_line * SCR_BREEDTE}\u2528\n"
    scr_frame += WAARSCHUWING_PLEK
    scr_frame += f"\u2517{horizontal_line * SCR_BREEDTE}\u251B"

    return scr_frame


#menu lijst maken
def maak_menu_lijst():
    menu_lijst =["1 - Toon Alle Orders",
                  "2 - Totale Omzet",
                  "3 - Aantal Orders",
                  "4 - Duurste Product",
                  "5 - Stoppen"]
    return menu_lijst


#voeg de menu aan de hoofdscherm
def toevoeg_menu_aanhoofdscherm(hoofdscherm_sjablon, menu_lijst):
    spatie = " "
    src_sjablon = hoofdscherm_sjablon
    menu_lijn_sjablon = f"\u2503{ spatie * 10 + MENU_TEKSTEN_PLEK + spatie * (SCR_BREEDTE - 30) }\u2503\n"
    menu_tekst = ""
    for menu in menu_lijst:
        menu_tekst += menu_lijn_sjablon.replace(MENU_TEKSTEN_PLEK, menu.ljust(20))
    src_sjablon = src_sjablon.replace(MENU_PLEK, menu_tekst)
    return src_sjablon


#voeg de inhouden aan de hoofdscherm
def toevoeg_inhoud_aanhoofdscherm(hoofdscherm_sjablon, inhouden):
    spatie = " "
    src_sjablon = hoofdscherm_sjablon
    inhoud_lijn_sjablon = f"\u2503{RESULTAAT_TEKSTEN_PLEK}\u2503\n"
    inhoud_tekst = ""
    for inhoud in inhouden:
        inhoud_tekst += inhoud_lijn_sjablon.replace(RESULTAAT_TEKSTEN_PLEK, inhoud)
    src_sjablon = src_sjablon.replace(RESULTAAT_PLEK, inhoud_tekst)
    return src_sjablon


#voeg de waarschuwing aan de hoofdscherm
def toevoeg_waarschuwing_aanhoofdscherm(hoofdscherm_sjablon, inhouden):
    spatie = " "
    src_sjablon = hoofdscherm_sjablon
    inhoud_lijn_sjablon = f"\u2503\033[31m{WAARSCHUWING_TEKSTEN_PLEK }\033[0m\u2503\n"
    inhoud_tekst = ""
    for inhoud in inhouden:
        inhoud_tekst += inhoud_lijn_sjablon.replace(WAARSCHUWING_TEKSTEN_PLEK, inhoud)
    src_sjablon = src_sjablon.replace(WAARSCHUWING_PLEK, inhoud_tekst)
    return src_sjablon


def voorbereid_bericht(bericht):
    bericht_lijst = []
    xbericht = bericht.ljust(SCR_BREEDTE)
    bericht_lijst.append(xbericht)
    #scr = toevoeg_waarschuwing_aanhoofdscherm(maak_hoofdscherm(), bericht_lijst)
    return bericht_lijst


#Laad de order lijst
def laad_order_lijst():
    order_lijst.append({"productnaam" : "USB-C Hub", "klant":"Sanne Bakker" , "aantal" : 2, "prijs": 35.00})
    order_lijst.append({"productnaam" : "Draadlose Muis", "klant":"Jan de Jong" , "aantal" : 2, "prijs": 24.99})
    order_lijst.append({"productnaam" : "Mechanisch Toetsenbord", "klant": "Sanne Bakker", "aantal": 1, "prijs":24.99})
    order_lijst.append({"productnaam" : "27-inch Monitor", "klant": "Lars van Dijk", "aantal": 1, "prijs": 249.00})
    order_lijst.append({"productnaam" : "USB-C Hub", "klant": "Fleur de Vries", "aantal": 3, "prijs": 35.00})
    order_lijst.append({"productnaam" : "Ergonomische Stoel", "klant": ",aan Jansen", "aantal":1, "prijs": 199.99})
    order_lijst.append({"productnaam" : "Koptelefoon", "klant": "Emma Visser", "aantal": 2, "prijs": 79.95})
    order_lijst.append({"productnaam" : "Laptop Standaard", "klant":"Milan Smit" , "aantal": 4, "prijs": 29.99})
    order_lijst.append({"productnaam" : "Webcam Full HD", "klant": "Sophie Mulder", "aantal": 2, "prijs": 59.90})
    order_lijst.append({"productnaam" : "Externe SSD 1TB", "klant": "Bram de Wit", "aantal": 2, "prijs": 119.00})
    order_lijst.append({"productnaam" : "Muismat XL", "klant": "Lotte Bos", "aantal": 5, "prijs": 14.50})
    order_lijst.append({"productnaam" : "Bluetooth Luidspreker", "klant": "Thijs Vos", "aantal": 1, "prijs": 45.00})
    order_lijst.append({"productnaam" : "Kabelmanagement Set", "klant":"Anouk Hendriks" , "aantal": 3, "prijs": 12.95})
    order_lijst.append({"productnaam" : "Powerbank 20000mAh", "klant": "Luuk de Ruiter", "aantal": 2, "prijs": 39.99})
    order_lijst.append({"productnaam" : "LED Bureau-lamp", "klant": "Eva van Leeuwen", "aantal": 1, "prijs": 34.50})
    order_lijst.append({"productnaam" : "HDMI Kabel 3m", "klant": "Sem Brouwer", "aantal": 4, "prijs": 9.99})
    order_lijst.append({"productnaam" : "Koptelefoon", "klant": "Anouk Hendriks", "aantal": 2, "prijs": 79.95})
    order_lijst.append({"productnaam" : "27-inch Monitor", "klant": "Eva van Leeuwen", "aantal": 2, "prijs": 249.00})


# toon alle order
def toon_alle_orders():

    try:
        orders_lijst_table = []


        horizontal_line = "\u2501"
        #top line
        top_line_tekst = (f"\u250F{horizontal_line * COLUMN_PRODUCT_NAAM_BREEDTE}\u2533" +
                    f"{horizontal_line * COLUMN_KLANT_BREEDTE}\u2533" +
                    f"{horizontal_line * COLUMN_AANTAL_BREEDTE}\u2533" +
                    f"{horizontal_line * COLUMN_PRIJS_BREEDTE}\u2513")
        orders_lijst_table.append(top_line_tekst)

        # hoofd tekst
        hoofd_tekst = (f"\u2503\033[94m{TITLE_PRODUCT_NAAM.ljust(30)}" +
                      f"\033[0m\u2503\033[94m{TITLE_KLANT.ljust(30)}" +
                      f"\033[0m\u2503\033[94m{TITLE_AANTAL.ljust(10)}" +
                      f"\033[0m\u2503\033[94m{TITLE_PRIJS.ljust(10)}" +
                      f"\033[0m\u2503")
        orders_lijst_table.append(hoofd_tekst)


        #schijdingsline
        schijdingsline_tekst = (f"\u2523{horizontal_line * COLUMN_PRODUCT_NAAM_BREEDTE}\u2528" +
                      f"{horizontal_line * COLUMN_KLANT_BREEDTE}\u2528" +
                      f"{horizontal_line * COLUMN_AANTAL_BREEDTE}\u2528" +
                      f"{horizontal_line * COLUMN_PRIJS_BREEDTE}\u2528")
        orders_lijst_table.append(schijdingsline_tekst)

        for order in order_lijst:
            productnaam = order["productnaam"]
            klant=order["klant"]
            aantal=str(order["aantal"])
            prijs_float = float(order["prijs"])
            prijs_str="%.2f" % prijs_float


            #order lijst
            orders_tekst = (f"\u2503{productnaam.ljust(30)}" +
                  f"\u2503{klant.ljust(30)}" +
                  f"\u2503{aantal.rjust(10)}" +
                  f"\u2503{prijs_str.rjust(10)}"
                  f"\u2503")
            orders_lijst_table.append(orders_tekst)


        #beneden horizontal line
        beneden_lijn_tekst = (f"\u2517{horizontal_line * COLUMN_PRODUCT_NAAM_BREEDTE}\u253B" +
              f"{horizontal_line * COLUMN_KLANT_BREEDTE}\u253B" +
              f"{horizontal_line * COLUMN_AANTAL_BREEDTE}\u253B" +
              f"{horizontal_line * COLUMN_PRIJS_BREEDTE}\u251B")
        orders_lijst_table.append(beneden_lijn_tekst)

        scr = toevoeg_inhoud_aanhoofdscherm(maak_hoofdscherm(), orders_lijst_table )

        hoofdscherm_sjablon_scr = scr
        lege_tekst = voorbereid_bericht(" ")
        hoofdscherm_sjablon_scr = toevoeg_inhoud_aanhoofdscherm(hoofdscherm_sjablon_scr, lege_tekst)
        hoofdscherm_sjablon_scr = toevoeg_waarschuwing_aanhoofdscherm(hoofdscherm_sjablon_scr, lege_tekst)
        print(hoofdscherm_sjablon_scr) # teken hoofd scherm

    except TypeError as e:
        # teken de sjabloon
        hoofdscherm_sjablon_scr = maak_hoofdscherm()
        lege_tekst = voorbereid_bericht(" ")
        hoofdscherm_sjablon_scr = toevoeg_inhoud_aanhoofdscherm(hoofdscherm_sjablon_scr, lege_tekst)
        waarschuwing_tekst = (f"{e}")
        hoofdscherm_sjablon_scr = toevoeg_waarschuwing_aanhoofdscherm(hoofdscherm_sjablon_scr,
                                                                      voorbereid_bericht(waarschuwing_tekst))
        print(hoofdscherm_sjablon_scr)


#bereken totale omzet
def bereken_totale_omzet() :
    try:
        orderkosten = 10
        totale_omzet = 0
        order_aantal = len(order_lijst)
        for order in order_lijst: #bereken totale omzet
            orderkosten = int(order["aantal"]) * float(order["prijs"])
            totale_omzet += orderkosten

        totale_omzet_str = "%.2f" % totale_omzet

        omzet_tekst = ""
        omzet_tekst_table = []

        horizontal_line = "\u2501"
        # top line
        top_line_tekst = (f"\u250F{horizontal_line * (SCR_BREEDTE-2)}\u2513")
        omzet_tekst_table.append(top_line_tekst)

        # Hoofd Tekst
        hoofd_tekst = (f"\u2503\033[94m\033[1m{OMZET_TITLE.center(SCR_BREEDTE-2)}\033[0m\u2503")
        omzet_tekst_table.append(hoofd_tekst)

        # schijdingsline
        schijdingsline_tekst = (f"\u2523{horizontal_line * (SCR_BREEDTE-2)}\u2528")
        omzet_tekst_table.append(schijdingsline_tekst)

        #lege line
        legeline_tekst = (f"\u2503{" " * (SCR_BREEDTE-2)}\u2503")
        omzet_tekst_table.append(legeline_tekst)
        omzet_tekst_table.append(legeline_tekst)
        omzet_tekst_table.append(legeline_tekst)

        # tekst lines
        midden_line_tekst = (f"\u2503    {(f"*_{order_aantal}_* orders verwerkt").ljust(SCR_BREEDTE-2)}\u2503")
        midden_line_tekst = midden_line_tekst.replace("*_","\033[31m\033[1m") #\033[32m\033[1m - \033[0m
        midden_line_tekst = midden_line_tekst.replace("_*", "\033[0m")  #verander de tekst om kleur te maken.
        omzet_tekst_table.append(midden_line_tekst)

        midden_line_tekst = (f"\u2503    {(f"Totale omzet       : *_{totale_omzet_str}").ljust(SCR_BREEDTE-8)}_*\u2503")
        midden_line_tekst = midden_line_tekst.replace("*_","  \033[32m\033[1m") #\033[32m\033[1m - \033[0m
        midden_line_tekst = midden_line_tekst.replace("_*", "  \033[0m")  #verander de tekst om kleur te maken.
        omzet_tekst_table.append(midden_line_tekst)

        omzet_tekst_table.append(legeline_tekst)
        omzet_tekst_table.append(legeline_tekst)

        # beneden horizontal line
        beneden_lijn_tekst = (f"\u2517{horizontal_line * (SCR_BREEDTE-2)}\u251B")
        omzet_tekst_table.append(beneden_lijn_tekst)

        #voeg aan het sjablon toe
        scr = toevoeg_inhoud_aanhoofdscherm(maak_hoofdscherm(), omzet_tekst_table)
        hoofdscherm_sjablon_scr = scr
        lege_tekst = voorbereid_bericht(" ")
        hoofdscherm_sjablon_scr = toevoeg_inhoud_aanhoofdscherm(hoofdscherm_sjablon_scr, lege_tekst)
        hoofdscherm_sjablon_scr = toevoeg_waarschuwing_aanhoofdscherm(hoofdscherm_sjablon_scr, lege_tekst)
        print(hoofdscherm_sjablon_scr) # teken hoofd scherm
    except TypeError as e:
        # teken de sjabloon
        hoofdscherm_sjablon_scr = maak_hoofdscherm()
        lege_tekst = voorbereid_bericht(" ")
        hoofdscherm_sjablon_scr = toevoeg_inhoud_aanhoofdscherm(hoofdscherm_sjablon_scr, lege_tekst)
        waarschuwing_tekst = (f"Controleer de gegevens. Een van aantal of prijs is geen nummer.")
        hoofdscherm_sjablon_scr = toevoeg_waarschuwing_aanhoofdscherm(hoofdscherm_sjablon_scr,
                                                                      voorbereid_bericht(waarschuwing_tekst))
        print(hoofdscherm_sjablon_scr)


#toon het  duurste product
def toon_duurste_product():
    #try:
    duurste_product = []

    duur_prijs = 0
    for order in order_lijst:
        if duur_prijs < float(order["prijs"]):
            duur_prijs = order["prijs"]
            duurste_product.clear()
            duurste_product.append(
                    {"productnaam" : order["productnaam"],
                    "klant": order["klant"] ,
                    "aantal" : order["aantal"],
                    "prijs": order["prijs"]})
        elif duur_prijs == float(order["prijs"]):
            duurste_product.append(
                    {"productnaam": order["productnaam"],
                     "klant": order["klant"],
                     "aantal": order["aantal"],
                     "prijs": order["prijs"]})


    duurste_product_tekst = ""
    duurste_product_tekst_table = []

    #begin met eerste tabel
    horizontal_line = "\u2501"
    # top meer line: eerste table
    top_line_tekst = (f"\u250F{horizontal_line * (SCR_BREEDTE - 2)}\u2513")
    duurste_product_tekst_table.append(top_line_tekst)

    # Hoofd Tekst
    hoofd_tekst = (f"\u2503\033[94m\033[1m{DUURSTE_PRODUCT_TITLE.center(SCR_BREEDTE - 2)}\033[0m\u2503")
    duurste_product_tekst_table.append(hoofd_tekst)

    # schijdingsline
    schijdingsline_tekst = (f"\u2523{horizontal_line * (SCR_BREEDTE - 2)}\u2528")
    duurste_product_tekst_table.append(schijdingsline_tekst)

    # lege line
    legeline_tekst = (f"\u2503{" " * (SCR_BREEDTE - 2)}\u2503")
    duurste_product_tekst_table.append(legeline_tekst)
    duurste_product_tekst_table.append(legeline_tekst)
    duurste_product_tekst_table.append(legeline_tekst)

    #begin met tweede table
    # top line
    top_line_tekst = (f"\u2503\u250F{horizontal_line * (COLUMN_PRODUCT_NAAM_BREEDTE + COLUMN_KLANT_BREEDTE +  COLUMN_AANTAL_BREEDTE )}\u2533" +
                      #f"{horizontal_line * COLUMN_KLANT_BREEDTE}\u2533" +
                      #f"{horizontal_line * COLUMN_AANTAL_BREEDTE}\u2533" +
                      f"{horizontal_line * (COLUMN_PRIJS_BREEDTE)}\u2513\u2503")
    duurste_product_tekst_table.append(top_line_tekst)

    #toevoegen table titles aan de tweede table
    hoofd_tekst = (f"\u2503\u2503\033[94m{TITLE_PRODUCT_NAAM.ljust(COLUMN_PRODUCT_NAAM_BREEDTE + COLUMN_KLANT_BREEDTE +  COLUMN_AANTAL_BREEDTE)}" +
                   #f"\033[0m\u2503\033[94m{TITLE_KLANT.ljust(30)}" +
                   #f"\033[0m\u2503\033[94m{TITLE_AANTAL.ljust(10)}" +
                   f"\033[0m\u2503\033[94m{TITLE_PRIJS.ljust(COLUMN_PRIJS_BREEDTE)}" +
                   f"\033[0m\u2503\u2503")
    duurste_product_tekst_table.append(hoofd_tekst)

    # schijdingsline van de tweede table
    schijdingsline_tekst = (f"\u2503\u2523{horizontal_line * (COLUMN_PRODUCT_NAAM_BREEDTE + COLUMN_KLANT_BREEDTE +  COLUMN_AANTAL_BREEDTE)}\u2528" +
                            #f"{horizontal_line * COLUMN_KLANT_BREEDTE}\u2528" +
                            #f"{horizontal_line * COLUMN_AANTAL_BREEDTE}\u2528" +
                            f"{horizontal_line * (COLUMN_PRIJS_BREEDTE)}\u2528\u2503")
    duurste_product_tekst_table.append(schijdingsline_tekst)

    # order lijst
    if len(duurste_product) > 0:
        for order in duurste_product:
            productnaam = order["productnaam"]
            klant = order["klant"]
            aantal = str(order["aantal"])
            prijs_float = float(order["prijs"])
            prijs_str = "%.2f" % prijs_float
            orders_tekst = (f"\u2503\u2503{productnaam.ljust(COLUMN_PRODUCT_NAAM_BREEDTE + COLUMN_KLANT_BREEDTE +  COLUMN_AANTAL_BREEDTE)}" +
                            #f"\u2503{klant.ljust(30)}" +
                            #f"\u2503{(aantal).rjust(10)}" +
                            f"\u2503{(prijs_str).rjust(COLUMN_PRIJS_BREEDTE)}" +
                            f"\u2503\u2503")
            duurste_product_tekst_table.append(orders_tekst)

    # beneden horizontal line
    beneden_lijn_tekst = (f"\u2503\u2517{horizontal_line * (COLUMN_PRODUCT_NAAM_BREEDTE + COLUMN_KLANT_BREEDTE +  COLUMN_AANTAL_BREEDTE)}\u253B" +
                          #f"{horizontal_line * COLUMN_KLANT_BREEDTE}\u253B" +
                          #f"{horizontal_line * COLUMN_AANTAL_BREEDTE}\u253B" +
                          f"{horizontal_line * (COLUMN_PRIJS_BREEDTE)}\u251B\u2503")
    duurste_product_tekst_table.append(beneden_lijn_tekst)
    #eind van tweede table

    #doorgan met de eerste table
    #lege line
    duurste_product_tekst_table.append(legeline_tekst)
    duurste_product_tekst_table.append(legeline_tekst)
    duurste_product_tekst_table.append(legeline_tekst)

    # beneden horizontal line
    beneden_lijn_tekst = (f"\u2517{horizontal_line * (SCR_BREEDTE-2)}\u251B")
    duurste_product_tekst_table.append(beneden_lijn_tekst)
    #eind van de eerste table


    #voeg aan het sjablon toe
    scr = toevoeg_inhoud_aanhoofdscherm(maak_hoofdscherm(), duurste_product_tekst_table)
    hoofdscherm_sjablon_scr = scr
    lege_tekst = voorbereid_bericht(" ")
    hoofdscherm_sjablon_scr = toevoeg_inhoud_aanhoofdscherm(hoofdscherm_sjablon_scr, lege_tekst)
    hoofdscherm_sjablon_scr = toevoeg_waarschuwing_aanhoofdscherm(hoofdscherm_sjablon_scr, lege_tekst)
    print(hoofdscherm_sjablon_scr)  # teken hoofd scherm


#toon aantal orders
def aantal_orders():
    order_aantal = len(order_lijst) #aantal orders
    product_aantal = 0
    for order in order_lijst:
        product_aantal += int(order["aantal"])

    aantal_orders_tekst = ""
    aantal_orders_tekst_table = []

    horizontal_line = "\u2501"
    # top line
    top_line_tekst = (f"\u250F{horizontal_line * (SCR_BREEDTE - 2)}\u2513")
    aantal_orders_tekst_table.append(top_line_tekst)

    # Hoofd Tekst
    hoofd_tekst = (f"\u2503\033[94m\033[1m{AANTAL_ORDERS_TITLE.center(SCR_BREEDTE - 2)}\033[0m\u2503")
    aantal_orders_tekst_table.append(hoofd_tekst)

    # schijdingsline
    schijdingsline_tekst = (f"\u2523{horizontal_line * (SCR_BREEDTE - 2)}\u2528")
    aantal_orders_tekst_table.append(schijdingsline_tekst)

    # lege line
    legeline_tekst = (f"\u2503{" " * (SCR_BREEDTE - 2)}\u2503")
    aantal_orders_tekst_table.append(legeline_tekst)
    aantal_orders_tekst_table.append(legeline_tekst)
    aantal_orders_tekst_table.append(legeline_tekst)

    # tekst lines
    midden_line_tekst = (f"\u2503    {(f"*_{order_aantal}_* orders verwerkt").ljust(SCR_BREEDTE-2)}\u2503")
    midden_line_tekst = midden_line_tekst.replace("*_", "\033[31m\033[1m")  # \033[32m\033[1m - \033[0m
    midden_line_tekst = midden_line_tekst.replace("_*", "\033[0m")  # verander de tekst om kleur te maken
    aantal_orders_tekst_table.append(midden_line_tekst)
    midden_line_tekst = (f"\u2503    {(f"Totale product     :    *_{product_aantal}_* ").ljust(SCR_BREEDTE-2)}\u2503")
    midden_line_tekst = midden_line_tekst.replace("*_", "\033[32m\033[1m")  # \033[32m\033[1m - \033[0m
    midden_line_tekst = midden_line_tekst.replace("_*", "\033[0m")  # verander de tekst om kleur te maken
    aantal_orders_tekst_table.append(midden_line_tekst)

    aantal_orders_tekst_table.append(legeline_tekst)
    aantal_orders_tekst_table.append(legeline_tekst)

    # beneden horizontal line
    beneden_lijn_tekst = (f"\u2517{horizontal_line * (SCR_BREEDTE - 2)}\u251B")
    aantal_orders_tekst_table.append(beneden_lijn_tekst)

    # voeg aan het sjablon toe
    scr = toevoeg_inhoud_aanhoofdscherm(maak_hoofdscherm(), aantal_orders_tekst_table)
    hoofdscherm_sjablon_scr = scr
    lege_tekst = voorbereid_bericht(" ")
    hoofdscherm_sjablon_scr = toevoeg_inhoud_aanhoofdscherm(hoofdscherm_sjablon_scr, lege_tekst)
    hoofdscherm_sjablon_scr = toevoeg_waarschuwing_aanhoofdscherm(hoofdscherm_sjablon_scr, lege_tekst)
    print(hoofdscherm_sjablon_scr)  # teken hoofd scherm



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    laad_order_lijst()
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
