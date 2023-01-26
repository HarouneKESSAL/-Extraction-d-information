
import sqlite3

from bs4 import BeautifulSoup

f = open('/home/swift/Unitex-GramLab-3.3/App/corpus-medical_snt/concord.html', 'r', encoding='utf-8').read()

table = []

soup = BeautifulSoup(f, 'html.parser')

lind = soup.findAll('a')

for i in lind:

    vec = i.text

    table.append(vec)

print(len(table))

zx = sqlite3.connect('extraction.db')

k = zx.cursor()

k.execute("DROP TABLE IF EXISTS extraction")

k.execute("CREATE TABLE extraction(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Posologie TEXT)")

k.executemany("INSERT INTO extraction(Posologie) VALUES(?)", [(x,) for x in table])

k.execute('select * from extraction')

print(k.fetchall())

zx.commit()

k.close()

zx.close()
