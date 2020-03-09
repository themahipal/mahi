#reliance stock prices
#all the imports

from bs4 import BeautifulSoup as bsoup
import requests

#class so that it can be called for a number of times
def relstock():
    r=requests.get("https://in.finance.yahoo.com/quote/RELIANCE.NS?p=RELIANCE.NS")
    soup=bsoup(r.text,"lxml")
    content = soup.find('div',class_="My(6px) Pos(r) smartphone_Mt(6px)").find('span').text
    return content

#Any type condition for looping
while True:
    print("Reliance Stock price :"+str(relstock()))
