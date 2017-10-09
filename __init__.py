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
DOMAINS_TO_PROCESS = "similarweb_list.dat"
FIELD_NAMES = ['site', 'web-servers', 'javascript-frameworks', 'tag-managers', 'programming-languages', 'databases', 'web-frameworks', 'cms', 'blogs', 'operating-systems', 'miscellaneous', 'video-players' ]
rawResultFile = open("raw_results.dat", "w")
pornsites = open(DOMAINS_TO_PROCESS, "r").read().splitlines()
table = PrettyTable()
table.field_names = FIELD_NAMES
for site in pornsites:
    print site
    data = ast.literal_eval(json.dumps(builtwith('http://' + site)))
    data['site'] = [site]
    rawResultFile.write(str(data) + '\n')
    row = []
    for k in FIELD_NAMES:
        try:
            fieldInfo = data[k]
        except KeyError:
            fieldInfo = ' '
            pass
        row.append(" ,".join(fieldInfo))

    table.add_row(row)

table_txt = table.get_string()
with open('formatted_results.dat','w') as file:
    file.write(table_txt)

