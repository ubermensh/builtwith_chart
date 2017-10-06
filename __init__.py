from urllib import urlopen
from bs4 import BeautifulSoup
from builtwith import builtwith
bw = builtwith('http://cam4.com')
print(bw)

'''
file = open("short.dat", "r")
pornsites = file.read().splitlines()
for site in pornsites:
    res = builtwith('http://' + site)
    print res
'''

# webpage = urlopen('https://www.cam4.com/').read()
# soup = BeautifulSoup(webpage, 'lxml')
# metas = soup.find_all("meta")
# print(type(metas))
# print(pornsites[955])
