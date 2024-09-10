for web scrapping, first install beautifulsoup
pip install beautifulsoap4
we need lxml library to install  
pip install ixml 



from bs4 import BeautifulSoup

with open


import requests

def fetchandsavetofile(url, path):
r = request.get(url)
with open(path, "w")
f.write(r.text)

url = "url of website"


r = request.get(url)
print(r.text)


import requests
from bs4 import BeautifulSoap


with open("sample.html", r) as f:
html_doc = f read()

soup = BeautifulSoap(html_doc, 'html.parser')
print(soup.pretiffy())
print(soup.title.string, type(soup.title))
print(soup.div)
print(soup.find_all("div")[1])



for link in soup.find_all("a");
printlink.get("href")


import request

from bs4 import beautifulSoup



with open("sample.html", "r") as f:
html doc = f read()


soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
print(soup.title, type(soup.title.string))
print(soup.div)
print(type(soup.find_all("div")[0]))

for link in soup.find_all("a"):
print(link.get("href"))
print(link.get("href").get_text)
soup.find(id="link3")


print(s.href)

print(soup.select("div"))

for child in soup.find(class_="container").children:
    print(child)

for parent in soup.find(class_="box").parents:
    print(parent)

cont = soup.find(class_= "container")
cont.name ="span"
cont["class"] = "my class"

cont.string="I am string"
print(cont)

ulTag = soup.new_tag("ul")
ulTag.append(liTag)

soup.html.body.insert(0, )

with open("modified.html")

def has_class_but_not_id(tag):
    return tag.has_attr("class")