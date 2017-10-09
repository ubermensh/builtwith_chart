from urllib import urlopen
from bs4 import BeautifulSoup
from builtwith import builtwith
from prettytable import PrettyTable
import json, ast, pprint

# bw = builtwith('http://cam4.com')
# print(bw)

# res = json.dumps({u'web-servers': [u'Nginx'], u'javascript-frameworks': [u'Prototype', u'RequireJS', u'jQuery'], u'tag-managers': [u'Google Tag Manager'], u'programming-languages': [u'Java'], u'databases': [u'Firebase'], u'web-frameworks': [u'Twitter Bootstrap']})
'''
dct  = ({'site': ['porn.com'], u'web-servers': [u'Nginx'], u'javascript-frameworks': [u'Prototype', u'RequireJS', u'jQuery'], u'tag-managers': [u'Google Tag Manager'], u'programming-languages': [u'Java'], u'databases': [u'Firebase'], u'web-frameworks': [u'Twitter Bootstrap']})
data = ast.literal_eval(json.dumps(dct))
print data.keys()
site = 'aaaa'
data['site'] = [site]
table = PrettyTable()
table.field_names = data.keys()
row = []
for k in data.keys():
    row.append(" ,".join(data[k]))
table.add_row(row)
print table
'''

rawResultFile = open("rawResults.dat", "w")
pornsites = open("short.dat", "r").read().splitlines()
table = PrettyTable()
FIELD_NAMES = ['site', 'web-servers', 'javascript-frameworks', 'tag-managers', 'programming-languages', 'databases', 'web-frameworks', 'cms', 'blogs', 'operating-systems', 'miscellaneous', 'video-players' ]
table.field_names = FIELD_NAMES
for site in pornsites:
    print site
    data = ast.literal_eval(json.dumps(builtwith('http://' + site)))
    data['site'] = [site]
    rawResultFile.write(str(data) + '/n')

    row = []
    for k in FIELD_NAMES:
        try:
            fieldInfo = data[k]
        except KeyError:
            fieldInfo = ' '
            pass
        row.append(" ,".join(fieldInfo))

    table.add_row(row)

# resultFile.write(table)
table_txt = table.get_string()
with open('results.dat','w') as file:
    file.write(table_txt)


# webpage = urlopen('https://www.cam4.com/').read()
# soup = BeautifulSoup(webpage, 'lxml')
# metas = soup.find_all("meta")
# print(type(metas))
# print(pornsites[955])
