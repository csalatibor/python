import random
szam1 = int(input('írj be egy számot! '))
szam2 = random.randint(10, 50)
SZAM3 = 5

szamok=[szam1,szam2, SZAM3]

with open('csalatibor.txt', 'w') as celfajl:
    for elem in szamok:
        celfajl.write(str(elem)+'\n')