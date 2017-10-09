from urllib import urlopen
from bs4 import BeautifulSoup
from builtwith import builtwith
import json, ast

# bw = builtwith('http://cam4.com')
# print(bw)

# res = json.dumps({u'web-servers': [u'Nginx'], u'javascript-frameworks': [u'Prototype', u'RequireJS', u'jQuery'], u'tag-managers': [u'Google Tag Manager'], u'programming-languages': [u'Java'], u'databases': [u'Firebase'], u'web-frameworks': [u'Twitter Bootstrap']})
dct  = ({u'web-servers': [u'Nginx'], u'javascript-frameworks': [u'Prototype', u'RequireJS', u'jQuery'], u'tag-managers': [u'Google Tag Manager'], u'programming-languages': [u'Java'], u'databases': [u'Firebase'], u'web-frameworks': [u'Twitter Bootstrap']})
data = ast.literal_eval(json.dumps(dct))
print(data.keys())
print(data['web-servers'])
# resultFile = open("results.dat", "w")
# pornsites = open("short.dat", "r").read().splitlines()
# for site in pornsites:
    # res = builtwith('http://' + site)
    # resultFile.write(site +': ' +  res + '\n')
    # print res
    # exit()

# webpage = urlopen('https://www.cam4.com/').read()
# soup = BeautifulSoup(webpage, 'lxml')
# metas = soup.find_all("meta")
# print(type(metas))
# print(pornsites[955])
