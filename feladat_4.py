import random
szam1 = int(input('írj be egy számot! '))
szam2 = random.randint(10, 50)
SZAM3 = 5

szamok=[szam1,szam2, SZAM3]
print(szamok)

print('a lista elemei növekvő sorrendben')
szamok.sort()
print(szamok)

print('a lista elemei csökkenő sorrendben')
szamok.reverse()
print(szamok)

print('a listához a 123 hozzáfűzve')
szamok.append(123)
print(szamok)

print('a listába a 3. helyre a 22 beszúrva')
szamok.insert(2, 22)
print(szamok)

print('a listaelemek törölve')
szamok.clear()
print(szamok)