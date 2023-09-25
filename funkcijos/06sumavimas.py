#parasyti programa kuri sudeda 2 skaicius (su funkcijomis)

def ivedimas(txt):
    sk=int(input(f'{txt}=...'))
    return sk

def sumavimas():
    sk1 = ivedimas('pirmas')
    sk2 = ivedimas('antras')
    suma = sk1 + sk2
    return suma, sk1, sk2

def rezultatas():
    sum, a, b = sumavimas()
    print(f'{a}+{b}={sum}')


rezultatas()