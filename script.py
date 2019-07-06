import requests
import sys
from bs4 import BeautifulSoup as bs


def date(year):
    year=year
    url = "https://en.wikipedia.org/wiki/"
    
    url += year + "_in_India"
    html = requests.get(url)
    soup = bs(html.content,'lxml')
   
    container = soup.find('div', {'class':'mw-content-ltr'})
    alList = container.findAll('h2')
    x=[]
    for a in alList:
        if a.find(text='Events'):
            data = a.findNext('ul').findAll("li")
    for d in data:
        print(d.text)

date(sys.argv[1])