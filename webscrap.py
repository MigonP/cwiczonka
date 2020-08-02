from urllib.request import urlopen, install_opener, OpenerDirector
from bs4 import BeautifulSoup

html = open('https://steamcommunity.com/sharedfiles/filedetails/?id=1497870430')
op = urlopen(str(html))
bs = BeautifulSoup(op.read(),'html.parser')
for tag in bs:
    

