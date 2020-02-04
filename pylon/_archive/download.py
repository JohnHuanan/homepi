import requests

image_url = "https://liquipedia.net/starcraft2/Premier_Tournaments.html"
  

r = requests.get(image_url) 
  
 
with open("start_neu.html",'wb') as f: 
    f.write(r.content) 