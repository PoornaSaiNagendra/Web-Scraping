from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

my_url = "https://en.wikipedia.org/wiki/Mahatma_Gandhi"

uClient = ureq(my_url)

page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

page_soup_div = page_soup.body.findAll("div", {"class" : "mw-parser-output"})
p = page_soup_div[0].findAll("p")

for i in range(0, len(p)):
    print(p[i].text)
