import csv
from pprint import pprint
new_file = None
with open('../data-398-2018-08-30.csv', 'r', encoding='cp1251') as file:
    file_with_content = csv.DictReader(file, delimiter=',')
    new_file = list(file_with_content)
print(1)
