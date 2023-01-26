import sys

import re


extrait = []
reg = r'''
    ^[-*Ø]?\s?  # Debut avec "* " ou "- "
    (\w+)       #La substance recherchée 
    \s:?\s?     #subts :  (GAVISCON : 1 sachet par jour.)
    (\d+|,|\d+.\d)+
    \s?:?   
    (\s(mg\s|MG|UI|ml|mcg|amp|iu|flacon|g|sachet|un\s|1/j|/j)(.+|\n)|(g|/j)\n|(mg)\s.+)
    '''
fa = open(sys.argv[1], 'r', encoding='UTF-8')

x = fa.readlines()

for i in x:


    regeou = re.search(reg, i, re.VERBOSE | re.I)

    if regeou:

        if regeou.group(1).lower() != 'vichy' \
                and regeou.group(1).lower() != 'mdz' \
                and regeou.group(1).lower() != 'vvp' \
                and regeou.group(1).lower() != 'hémoglobine' \
                and regeou.group(1).lower() != 'aspegic' \
                and regeou.group(1).lower() != 'kt' \
                and regeou.group(1).lower() != 'le' \
                and regeou.group(1).lower() != 'b1' \
                and regeou.group(1).lower() != 'puis':
            extrait.append(regeou.group(1).lower() + ',.N+subst' + '\n')
for i in x:

    regeou = re.search('((vitamine|VITAMINE|Vitamine) [A-Za-b](\d| \d)*)', i)

    if regeou:

        extrait.append(regeou.group(1).lower() + ',.N+subst' + '\n')

fa.close()

print(len(extrait))

extrait = sorted(list(set(extrait)))

p = open('subst_corpus.dic', 'w', encoding='UTF-16 LE')

p.write('\ufeff')

for i in extrait:

    p.write(i)

extrait = sorted(list(set(extrait)))


print(len(extrait))

f2 = open('res.txt', 'w', encoding='UTF-8')

for i in extrait:

    f2.write(i)

f2.close()

f2 = open('res.txt', 'r', encoding='UTF-8')

f = open('subst.dic', 'r', encoding='utf-16')

fo23 = open('infos3.txt', 'w', encoding='UTF-8')

reolu = f2.readlines()

reolsi = f.readlines()

reolu = sorted(list(set(reolu)))

reolsi = sorted(list(set(reolsi)))

s = 0

for let in 'abcdeéfghijklmnopqrstuvwxyz':

    c = 0

    for r in reolu:

        if r[0] == let:

            if r not in reolsi:

                fo23.write(r)

                c = c + 1

    fo23.write('-' * 100 + '\n')

    fo23.write(f'pour {let}:{str(c)}\n')

    fo23.write('-' * 100 + '\n')

    s = s + c

fo23.write(f'resultat a ajouter:{s}')

s = 0

f2 = open('res.txt', 'r', encoding='UTF-8')

f3 = open('infos2.txt', 'w', encoding='UTF-8')

for lettre in 'abcdeéfghijklmnopqrstuvwxyz':

    for ext in extrait:

        if ext[0] == lettre:

            f3.write(ext)

            c = c + 1

    f3.write('-' * 100 + '\n')

    f3.write(f'total de {lettre}:{str(c)} \n')

    f3.write('-' * 100 + '\n')

    s = s + c

    c = 0

f3.write(f'Nombre de medicaments issus de corpus de corpus medical:{s} \n')

f3.close()

f2.close()


f2 = open('res.txt', 'r', encoding='UTF-8')

res = f2.readlines()

tab = []

for e in res:

    if e not in tab:

        tab.append(e)

f2.close()

f2 = open('res.txt', 'w', encoding='UTF-8')

for e in tab:

    f2.write(e)

f2.close()

f2 = open('res.txt', 'r', encoding='UTF-8')

res = f2.readlines()

f2.close()

f3 = open('subst.dic', 'r', encoding='utf-16')

x = f3.readlines()

for i in x:

    if i not in res:

        res.append(i)

res = sorted(list(set(res)))

f3.close()

f3 = open('subst.dic', 'w', encoding='utf-16')

f3.write('\ufeff')

for e in res:

    f3.write(e)

f3.close()
