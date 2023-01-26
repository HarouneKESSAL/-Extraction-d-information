import requests
from bs4 import BeautifulSoup
import sys

url = f'http://127.0.0.1:{str(sys.argv[2])}/vidal/'

ko = requests.get(url)

l: list[str] = []

fo = open('subst.dic', 'w', encoding='utf-16 LE')

fo1 = open('infos1.txt', 'w', encoding='utf-8')

fo.write('\ufeff')

fo1.write('\ufeff')

inte = sys.argv[1]

x = inte.split('-')

print(x)

ask = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

fir = ask.index(x[0])

las = ask.index(x[1])

for i in range(fir, las + 1):

    l.append(f'http://127.0.0.1:{str(sys.argv[2])}/vidal/vidal-Sommaires-Substances-{ask[i]}.html')

print(l)

p = 0

pq = 0

for link in l:

    url = link

    reponse = requests.get(url)

    if reponse.ok:

        s4 = BeautifulSoup(reponse.text, 'html.parser')

        liy = s4.findAll('ul', {'class': 'substances list_index has_children'})

        for ql in liy:

            liste = ql.findAll('li')

            for li in liste:

                ops = li.findAll('a')

                for i in ops:

                    voxpopuli = i.text

                    voxpopuli = voxpopuli.replace('Ã©', 'é')

                    voxpopuli = voxpopuli.replace('Ã¨', 'è')

                    voxpopuli = voxpopuli.replace('Ã¯', 'ï')

                    voxpopuli = voxpopuli.replace("Ãª", 'ê')

                    fo.write(voxpopuli + ',.N+subset ' + ' \n ')

                    p = p + 1

        fo1.write(f'pour {ask[fir]}:' + str(p) + '\n')

        fir = fir + 1

        pq = pq + p

        p = 0


fo1.write(f'somme:' + str(pq) + '\n')

fo.close()

fo1.close()
