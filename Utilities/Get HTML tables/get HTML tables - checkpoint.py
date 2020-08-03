'''


Start time: 6:10pm Aug 2nd 2020
Break: 7:50 pm
Resume: 9:24 pm
Done: 10:11pm               https://www.w3schools.com/html/html_tables.asp
Total time: 1:40 + 0:50 = 2:30
'''

import urllib.request
import pandas as pd

# URL = "http://www.python.org"
# URL = "https://en.wikipedia.org/wiki/Maginot_Line"
# URL = "https://ca.finance.yahoo.com/quote/AAPL/financials?p=AAPL"  # AAPL Stock
URL = "https://www.w3schools.com/html/html_tables.asp"
fp = urllib.request.urlopen(URL)
mybytes = fp.read()

mystr = mybytes.decode("utf8")

fp.close()

htmlSplit = mystr.split('\n')
# for i in htmlSplit:
#     print(i)
print(type(htmlSplit))  # list


def delete_tag_with_prarams(data, first_bit_of_first_tag='<a', closing_tag='</a>'):
    start_index = data.find(first_bit_of_first_tag)
    if start_index != -1:
        print('delete_tag_with_prarams PRE: ', data)
        end_index = data.find('>')
        # print(start_index, " | ", end_index)
        to_remove = data[start_index:end_index + 1]
        data = data.replace(to_remove, '').replace(closing_tag, '')
        print('delete_tag_with_prarams POST: ', data)
    return data


def clean(data):
    if len(data) == 0:
        return ''

    # print('will clean: ', data)

    if data[0] == '>':
        data = data[1:]

    strings_to_remove = ['<p>', '</p>', '<em>', '</em>', '<a>', '&lt;', '&gt;', '&le;', '&ge;']
    for i in strings_to_remove:
        data = data.replace(i, '')

    print('cleaning: ', data)
    data_copy = data
    data = delete_tag_with_prarams(data, '<a', '</a>')
    while data != data_copy:
        data_copy = data
        data = delete_tag_with_prarams(data, '<a', '</a>')
        # data = delete_tag_with_prarams(data, '<table', '</table>')
        print('it ran...')
    print('returning: ', data)
    return data


def process(lines):
    list_of_tables = []
    nested_array = []
    data = ''
    print('--------------------------------------------------------------------------------------------------------------------')
    for line in lines:

        if '</tr>' in line:
            list_of_tables.append(nested_array)
            nested_array = []

        nest = ''
        data = ''
        if '<th' in line:
            start_index = line.find('>')
            end_index = line.find('</')
            data += line[start_index:end_index]

            nest += clean(data)
            data = ''
        if '<td' in line:
            end_index = line.rfind('</')
            start_index = line.find('>')  # the last '>' is always the last index, so have a upper bound
            print(start_index, " | ", end_index)
            data += line[start_index + 1:end_index]
            nest += clean(data)

        # next to create: list of tables
        if len(nest) > 0:
            nested_array.append(nest)

    return list_of_tables


list_of_nested_arrays = []
nested_array = []
lines = []
flip = False

for line in htmlSplit:
    if '<table' in line:
        flip = True
        lines = []  # should* be clear in end instead, but will effect final print
    if flip:
        # show data
        print(line)
        lines.append(line)
    if '</table>' in line:
        flip = False
        nested_array = process(lines)
        list_of_nested_arrays.append(nested_array)
        for i in nested_array:
            print(i)
        # exit()

print('=========================================================')
for array in list_of_nested_arrays:
   print(pd.DataFrame(array).head())
