from builtwith import builtwith
from prettytable import PrettyTable
import json, ast, pprint
DOMAINS_TO_PROCESS = "input_sites/steve_list.dat"
FIELD_NAMES = ['site','analytics', 'web-servers', 'javascript-frameworks', 'tag-managers', 'programming-languages', 'databases', 'web-frameworks', 'operating-systems']
pornsites = open(DOMAINS_TO_PROCESS, "r").read().splitlines()
LIST_LENGTH = str(len(pornsites))
rawResultFile = open('raw_'+ DOMAINS_TO_PROCESS[12:],'w+')
table = PrettyTable()
table.field_names = FIELD_NAMES
n = 1
for site in pornsites:
    print str(n) + " of " + LIST_LENGTH + ": " + site
    n += 1
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
        row.append(", ".join(fieldInfo))

    print str(data)
    table.add_row(row)

table_txt = table.get_string()
with open('result_'+ DOMAINS_TO_PROCESS[12:],'w+') as file:
    file.write(table_txt)


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
