from bs4 import BeautifulSoup
import pandas
import  requests
import csv

Url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
html = requests.get(Url)
soup = BeautifulSoup(html.text, 'html.parser')

headers = ["Name", "Distance", "Mass", "Radius"]
names = []
dists = []
masses = []
radii = []

table_list = soup.find_all('table', class_= 'wikitable sortable')
table = table_list[2].find_all('tr')

# table_body contains the list of all the rows
table_body = table[1:]

for row in table_body:
    row_data = row.find_all('td')
    try:
        names.append(row_data[0].a.text)
        dists.append(row_data[5].text)
        masses.append(row_data[7].text)
        radii.append(row_data[8].text)
    except:
        names.append(row_data[0].text)
        dists.append(row_data[5].text)
        masses.append(row_data[7].text)
        radii.append(row_data[8].text)

for index, i in enumerate(names):
    if i == '':
        names[index] = '-'
for index, i in enumerate(dists):
    if i == '':
        dists[index] = '-'
for index, i in enumerate(masses):
    if i == '':
        masses[index] = '-'
for index, i in enumerate(radii):
    if i == '':
        radii[index] = '-'


with open("Field_brown_dwarfs.csv", "w", newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    for i in range(len(names)):
        try:
            csvwriter.writerow([names[i], dists[i], masses[i], radii[i]])
        except:
            csvwriter.writerow(["Error", "Error", "Error", "Error"])
