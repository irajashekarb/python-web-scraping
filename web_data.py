from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

url = 'https://community.smenet.org/network/members/advanced-search?ssopc=1'

uClient = uReq(url)
page_html = uClient.read()
uClient.close()
soup = BeautifulSoup(page_html, "html.parser")

print(soup.prettify())

containers = soup.findAll("div", {"class" : "row member-row ribbons"})
print(len(containers))
print(containers.text)
#print(soup.prettify(containers[0]))