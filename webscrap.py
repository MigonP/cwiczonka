from urllib.request import urlopen
from bs4 import BeautifulSoup

html = open('https://www.x-rates.com/table/?from=PLN&amount=1')
op = urlopen(str(html))
bs = BeautifulSoup(op.read(),'html.parser')
waluta = bs.find_all(class_="moduleContent")
for x in waluta:
    print(x.get_text())
    

