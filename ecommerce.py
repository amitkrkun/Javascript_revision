import requests
from bs4 import BeautifulSoup
import pandas as pd
 

data = {'title': [], 'col_2': ['a', 'b', 'c', 'd']}
data = {'title': [], 'price': []}
url = ""
headers = {}


soup = BeautifulSoup(r.text, 'html.parser')
spans = soup.select("span.a-size-medium.a-color-base.a-text-normal")
prices = soup.select("span.a-price")
for span in spans:
    print(span.string)
    data["title"].append(span.string)

for price in prices:
    print(price.string)
    print(price.children[0].get_text())


for price in prices:
    if("a-text-price" in price.get("class")):
        print(print.find("span").get_text())
        data["price"].append(price.find("span").get_text())
        if len(data["price"])==len(data["title"]):
            break

df = pd.DataFrame.from_dict(data)
df.to_csv("data.csv", index=False)



