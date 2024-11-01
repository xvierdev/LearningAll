# utilização de variáveis globais
ze = 'uniforme cinza'

def fatec():
    global ze
    ze = 'uniforme preto'
    print(ze)

print(ze)
fatec()
print(ze)

# funcão lambda

x = 8

print(lambda pow:x**2)