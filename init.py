from urllib import urlopen
from bs4 import BeautifulSoup
file = open("short.dat", "r")
pornsites = file.read().splitlines()
for site in pornsites:
    print site

webpage = urlopen('https://www.cam4.com/').read()
soup = BeautifulSoup(webpage, 'lxml')
metas = soup.find_all("meta")
print(type(metas))
# print(pornsites[955])
