#-*- coding:utf-8 -*-
import time                                                                             # Das time Modul benötigen wir um das aktuelle Datum bekommen zu können.
import os
import requests 

                                                                                        # Die folgende Funktion vergleicht das aktuelle Datum mit den Daten aus den Strings startString und endString... Dazu müssen der Funktion zwei Argumente übergeben werden in String-Form, die das Datum in der Form: JJJJ-MM-TT enthalten
def dateCompare(startString, endString):
    locTime = time.localtime()                                                          # Das aktuelle Datum wird durch die Funktion time.localtime() ermittelt und in der Variablen locTime gespeichert.
    if locTime[0] >= int(startString[0:4]) and locTime[0] <= int(endString[0:4]):       # locTime[0] beinhaltet das Jahr als integer. Der String wird nur an den Stellen 0 bis 4 eingelesen, denn dort steht das Jahr im Format JJJ-MM-TT. Wenn das aktuelle Jahr mit dem Jahr des übergebenen Strings übereinstimmt und kleiner/gleich dem EndJahr ist, ist die Bedingung erfüllt.
        yearTrue = True                                                                 # die Variable yearTrue wird erzeugt, die am Ende der Funktion angibt, ob das aktuelle Jahr mit den Jahren in startString und endString stehen übereinstimmt. Wenn es passt True, sonst False
    else:
        yearTrue = False
    if locTime[1] >= int(startString[5:7]) and locTime[1] <= int(endString[5:7]):       # alles wie unter Jahr. Jetzt nur mit Monat. Der aktuelle Monat ist in locTime[1] gespeichert. Im String an den Positionen 5:7. die Variable monthTrue wird auf True gesetzt       
        monthTrue = True
    else:
        monthTrue = False
    if locTime[2] >= int(startString[8:10]) and locTime[1] <= int(endString[8:10]):
        dayTrue = True
    else:
        dayTrue = False

    if yearTrue == True and monthTrue == True and dayTrue == True:                      # Jetzt wird geprüft, ob Jahr und Monat und Tag passen. Diese Art ist etwas umständlich. Weil wir eigentlich nur wissen wollen, ob das ganze Datum stimmt oder nicht. Die Erzeugung von Extra-Variablen für Jahr und Monat und Tag ist viel überflüssiger Aufwand. Zwischenzeitlich aber dadurch leichter nachvollziehbar, wo der Fehler sitzt.
        dateTrue = True
    else:
        dateTrue = False

    return dateTrue

def datenExtrahieren(datei):                                                            # An die Methode datenExtrahieren wird die zu dursuchende Datei als string übergeben. Die Methode sucht dann, ob in dieser Datei ein String vorkommt, der aus dem aktuellen Jahr und einem "-" besteht (z. B. 2019-). Warum? Weil in unserem Falle alle Daten der Tourniere eindeutig mit Jahreszahl- beginnen.
    input = open(datei)                                                                 # übergebene Datei wird geöffnet.
    text = input.read()                                                                 # der Inhalt der datei an text übergeben.
    locTime = time.localtime()                                                          # atuelles Datum wird ermittelt und in der Variable locTime gespeichert
    sub = str(locTime[0]) + "-"                                                         # aus der Variablen locTime wird das aktuelle Jahr entnommen und mit einem "-" versehen. Anschließend in dem String sub gespeichert.
    pos = 0                                                                             #
    while pos != -1:                                                                        # Solange pos nicht -1 wird, setzt sich die Schleife fort... pos wird dann -1, wenn die Methode text.find(sub) den sub-string nicht mehr findet.                                                                   
        pos = text.find(sub)                                                                # die gefundenen Positionen werden an pos übergeben
        if pos > 700:                                                                       # Sollte die gefunden Position größer als 700 Zeichen sind, wird der Inhalt der text-Variable an der Stelle von pos, inklusive des Inhalts der nächsten 10 Stellen an den String startDatum angehängt. Warum größer als 700? Ich habe festgestellt, dass zwischen Anfangs und End-Datum in der Datei in der Regel 400 bis 500 Zeichen liegen. Wenn mehr als 700 geht es demnach um ein neues Anfangs-Datum und nicht um das End-Datum, das zu dem Anfangs-Datum gehört.
            startDatum.append(text[pos:(pos+10)])
        if (pos > -1 and pos <700):                                                         # Wenn der Abstand unter 700 Zeichen ist, ist es hingegen wahrscheinlich das End-Datum und wird daher dem zugehörigen End-Datum String übergeben                                
            endDatum.append(text[pos:(pos+10)])
        text = text[(pos+10):]

syscode = 11000
geraetecode = 3

einschalten = "sudo /home/pi/rcswitch-pi/./send " + str(syscode) + " "+ str(geraetecode) + " " +"1"
ausschalten = "sudo /home/pi/rcswitch-pi/./send " + str(syscode) + " "+ str(geraetecode) + " " +"0"

os.system(ausschalten)

startDatum = []                                                                         # Wir definieren einen Array startDatum... In diesem sollen die Beginn-Daten aus der Datei eingetragen werden. In String-Form
endDatum = []                                                                           # Wir definieren einen Array endDatum...   In diesem sollen die End-Daten als Strings gespeichert werden.

image_url = "https://liquipedia.net/starcraft2/Premier_Tournaments"
  
r = requests.get(image_url) 
  
with open("star_neu.html",'wb') as f: 
    f.write(r.content) 

datenExtrahieren('star_neu.html')   

for i in range (0, (len(startDatum))):
    datumPasst = dateCompare(startDatum[i],endDatum[i])
    if datumPasst == True:
        os.system(einschalten)
        print("Lieber Fabian! Heute ist ein Starcraft-Turnier!")
        break
    else:
        print("Datum passt nicht!")
    

# to run this script daily either
# a) copy it to /etc/cron.daily
# b) or edit the /etc/crontab: Works as following:
#    1)open terminal.
#    2)change directory to /etc
#    3)type "sudo nano crontab"
#    4)settings for starting "47 1 * * * /home/pi/hompe/starcraft_final.py"
#    5)starcraft_final.py will be executed at 1.47

# source: http://raspberry.tips/raspberrypi-einsteiger/cronjob-auf-dem-raspberry-pi-einrichten

#os.system('Pause')
    

