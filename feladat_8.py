def alahuzas(alahuzas):
    print(alahuzas+'_')
    
with open('csalatibor.txt', 'r') as forras:
    for s in forras:
        alahuzas(s.strip())