import requests
import csv
from bs4 import BeautifulSoup


def get_cid(page):
    r = requests.get(page)
    soup = BeautifulSoup(r.content)
    # print(soup.prettify())
    #print(soup.title.contents[0])
    if soup.title.contents[0] == "No items found - PubChem Compound - NCBI":
        return "N/A"
    if "- PubChem Compound - NCBI" not in soup.title.contents[0]:
        #need to pull from <meta name="pubchem_uid_value" content="77553">
        metatag = soup.find(attrs={'name':'pubchem_uid_value'})
        #print(metatag['content'])
        return metatag['content']
    cids = soup.find_all('dd')
    count = 0
    for id in cids:
        if count == 4:
            return id.contents[0]
        else:
            count += 1
    # Fifth existence of <dd> tag will give us the CID of the top result


def sanitize(s):
    f = ""
    for c in s:
        if c == " ":
            f += "+"
        elif c == "-":
            f += "_"
        else:
            f += c
    return f
    # change spaces to + and dashes to underscores


def add_to_output(d,pid):
    with open(r'output.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([d, pid])
    return

with open('input.csv') as csv_file:
    # open csv file with only drug names in a single column, no header info
    csv_reader = csv.reader(csv_file, delimiter=',')
    druglist = []
    for row in csv_reader:
        druglist.append(row[0])

# populate druglist list with names of drugs

with open('output.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(["Drug","PubChemID"])
#initialize output file

for drugname in druglist:
    # insert function here to sanitize drugname so it can be used as an input
    drug = sanitize(drugname)
    url = 'https://www.ncbi.nlm.nih.gov/pccompound/?term=' + drug
    pubchemID = get_cid(url)
    add_to_output(drug,pubchemID)
    #break
    print(drug)

print("Success!")

