from builtwith import builtwith
from prettytable import PrettyTable
import json, ast, pprint
DOMAINS_TO_PROCESS = "input_sites/reddit_list.dat"
FIELD_NAMES = ['site','analytics', 'web-servers', 'javascript-frameworks', 'tag-managers', 'programming-languages', 'databases', 'web-frameworks', 'operating-systems']
sites_list = open(DOMAINS_TO_PROCESS, "r").read().splitlines()
LIST_LENGTH = str(len(sites_list))
def __makeRow(data):
    row = []
    for k in FIELD_NAMES:
        try:
            fieldInfo = data[k]
        except KeyError:
            fieldInfo = ' '
            pass
        row.append(", ".join(fieldInfo))
    return row

rawResultFile = open('raw_'+ DOMAINS_TO_PROCESS[12:],'w+')
table = PrettyTable()
table.field_names = FIELD_NAMES
n=1
for site in sites_list:
    print str(n) + " of " + LIST_LENGTH + ": " + site
    n+=1
    data = ast.literal_eval(json.dumps(builtwith('http://' + site)))
    data['site'] = [site]
    rawResultFile.write(str(data) + '\n')
    row = __makeRow(data)
    table.add_row(row)
    print str(data)


table_txt = table.get_string()
with open('result_'+ DOMAINS_TO_PROCESS[12:],'w+') as file:
    file.write(table_txt)

