import random
szam1 = int(input('írj be egy számot! '))
szam2 = random.randint(10, 50)
SZAM3 = 5
while szam2 % 2 != 1:
    szam2 = random.randint(10, 50)
if szam1 % 2 == 0:
    print('A beírt szám páros.')
else: print('A beírt szám páratlan')
print(szam1, szam2, SZAM3)