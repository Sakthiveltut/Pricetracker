import requests
from bs4 import BeautifulSoup
import re

url = "https://www.flipkart.com/search?q=Bluetooth Headphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=20"
response = requests.get(url)
data = BeautifulSoup(response.content,"html.parser")

rows = data.find_all("div","_75nlfW")
for row in rows:

    products = row.find_all("div",{'data-id':True})
    for product in products:

        price = product.find("div","Nx9bqj")
        if(price):
            print(re.sub(r'\D','',price.text))
            id = product["data-id"]
            print(id)

            title = product.find("a","wjcEIp")
            print(title["title"])

            images = product.find("img","DByuf4")
            print(images["src"])

            """offer = product.find("div","UkUFwK")
            print(offer.text)"""

            url = product.find("a","VJA3rP")
            print("https://flipkart.com"+url["href"])

            print("-----------------------------------------------")

"""
DOjaWF gdgoEp    - full

cPHDOP col-12-12

_75nlfW

DLLFFNVDYGQN9XCS     - id

_4WELSP   img
xgS27m    title
hl05eU   price
UkUFwK   offer

"""

