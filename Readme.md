# Brightstone Logistiek Orders Overzicht

**Brightstone Logistiek Orders Overzicht** is een lichtgewicht, interactieve Command Line Interface (CLI) applicatie ontwikkeld in **Python 3.14**. De software biedt een overzichtelijke visualisatie van bestelgegevens via een gestructureerd menu en een pseudo-windowed terminalinterface.

##  Projectinformatie

**Auteur**         : Burak Çekiç

**Team**           : Motopp ITNL4 Ontwikkelaar Team

**Versie**         : v1.0.0 

**Datum**          : September 2026 

**Python-versie**  : 3.14+ 

**Licentie**       : MIT License 

**Contact**        : burak.cekic@motopp.nl 

 

---

##  Functionaliteiten

De applicatie wordt aangestuurd vanuit een centraal hoofdmenu. Gebruikers kunnen via eenvoudige nummerselectie (1 t/m 5) de gewenste gegevens opvragen:

1. **Toon alle orders:** Geeft een gedetailleerde tabel weer van alle bestelde producten, inclusief klantinformatie, aantallen en prijzen.
2. **Totale omzet:** Berekent en toont de totale omzet over alle geregistreerde bestellingen.
3. **Aantal orders:** Geeft het exacte totale aantal totale orders weer.
4. **Duurste product:** Identificeert en toont het product met de hoogste verkoopprijs uit het overzicht.
5. **Stoppen:** Sluit de applicatie veilig af.

---

##  Kenmerken & Ontwerp

* **Geen Externe Afhankelijkheden:** Volledig gebouwd met de standaard Python-bibliotheek (*Standard Library*). Geen aanvullende `pip`-pakketten vereist.
* **Window-Like Gebruikerservaring:** De terminal wordt bij elke handeling ververst via schermreiniging (`os.system` / ANSI escape-codes). Hierdoor scrolt de uitvoer niet naar boven, maar werkt het programma als een dynamisch venster.
* **Geformatteerde Tabellen:** Maakt gebruik van Unicode-kadertekens (`┏`, `━`, `┓`, `│`) en string-uitlijning (`ljust`, `rjust`, `center`) voor een strakke, professionele tabelweergave.
* **Inheemse ANSI-kleuren:** Visuele accenten in menu's en tabellen worden voorzien via standaard ANSI-kleurcodes.

---

##  Vereisten

* **Python:** Versie 3.14 of hoger.
* **Besturingssysteem:** Windows, macOS of Linux.

---

##  Uitvoeren
Open uw terminal of opdrachtprompt, navigeer naar de betreffende map en start de applicatie met het volgende commando:

```bash
python brightstone.py