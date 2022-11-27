import random
szam1 = int(input('írj be egy számot! '))
szam2 = random.randint(10, 50)
SZAM3 = 5

halmaz={szam1, szam2, SZAM3}
print(halmaz)

print('a halmazhoz egy elem -34- hozzáadása')
halmaz.add(34)
print(halmaz)

print('a halmazból egy elem -5- törlése')
halmaz.remove(5)
print(halmaz)

e=halmaz.pop()
print('a halmazhoz egy elem -', e, ' - törlése')
print(halmaz)

print('a halmaz maradék elemeinek a törlése')
halmaz.clear()
print(halmaz)