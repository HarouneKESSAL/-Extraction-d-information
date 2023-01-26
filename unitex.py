import os

from os import path

if path.exists("corpus-medical_snt"):

    os.system("rd /s corpus-medical_snt")

os.mkdir("corpus-medical_snt")

os.system("UnitexToolLogger Normalize corpus-medical.txt -r Norm.txt")

os.system("UnitexToolLogger Tokenize corpus-medical.snt")

os.system("UnitexToolLogger Dico -t corpus-medical.snt Dela_fr.bin")

os.system("UnitexToolLogger Dico -t corpus-medical.snt Dela_fr.inf")

os.system("UnitexToolLogger Dico -t corpus-medical.snt subst.dic")

os.system("UnitexToolLogger Dico -t corpus-medical.snt subst.bin")

os.system("UnitexToolLogger Normalize -t corpus-medical.snt Alphabet.txt -r ")

os.system("UnitexToolLogger Grf2Fst2 pos.grf")

os.system("UnitexToolLogger Locate -t corpus-medical.snt pos.fst2 -L -I --all")

os.system("UnitexToolLogger Concord corpus-medical_snt/concord.ind -f \"Courrier new\" -s 12 -l 40 -r 55")

