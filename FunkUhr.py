import os
import time

syscode = 11000
geraetecode = 3

einschalten = "sudo /home/pi/rcswitch-pi/./send " + str(syscode) + " "+ str(geraetecode) + " " +"1"
ausschalten = "sudo /home/pi/rcswitch-pi/./send " + str(syscode) + " "+ str(geraetecode) + " " +"0"

while True:
    lt = time.localtime()
    h = lt[3]
    
    if h <= 21 and h >= 6:
        os.system(einschalten)
        print(einschalten)
    
    else:
        os.system(ausschalten)
        print(ausschalten)
        
    time.sleep(60) # eine Minute nichts tun
    print(lt)


