from bs4 import BeautifulSoup

with open("example.html", 'r') as f:
    content = f.read()
    # print(content)
soup = BeautifulSoup(content, 'html.parser')
# print(soup.prettify())
tags = soup.find_all("div")
for items in tags:
    print(items.p.text)

