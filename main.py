file = open('midwayusa.txt','r')
f = file.readlines()
lst=[]
for lines in f:
    lst.append(lines[:-1])

import pandas as pd
import requests
from bs4 import BeautifulSoup

def func(url):
    page = requests.get(url)
    if (page.status_code==200):
        Soup = BeautifulSoup(page.content,'html.parser')
        ProductTitle = Soup.find(attrs={'class':'text-left heading-main'}).text.replace('\n'," ").replace("\r"," ").strip()
        StockStatus = memo[Soup.find(attrs={'ng-bind':'selector.productAvailability'}).text.replace('\n'," ").replace("\r"," ").strip()]
        Hyperlink = url
        return [ProductTitle,StockStatus,Hyperlink]
    else:
        print(url,': Invalid request')

data=[]
memo={"Available":"In Stock","Temporarily Unavailable":"Out of Stock","Out of Stock":"Out of Stock","Mixed Availability":"Variant"}
for i in range(len(lst)):
    x = func(lst[i])
    if x!=None:
        data.append(x)
df = pd.DataFrame(data, columns=['Product Title','Stock Status','Hyperlink'])
df.to_csv('assignment.csv')
