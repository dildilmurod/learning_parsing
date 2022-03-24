
from bs4 import BeautifulSoup

with open("info/index.html", encoding='utf-8') as file:
    src = file.read()

# print(src)

soup = BeautifulSoup(src, "lxml")

title = soup.title

print(title)
