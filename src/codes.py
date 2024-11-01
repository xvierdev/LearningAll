# verifica se um número é par.
def e_par(n):
    if n% 2 == 0: return True
    else: return False

completos = ['wesley jesus', 'maria silva', 'leonora aparecida']
# completos.sort()

def sobrenome(completo):
    completo = completo.split()
    return completo[1]

completos.sort(key=sobrenome)
# print(completos)

# introdução ao uso de funções lambda

nome = 'joão silva'
completos.sort(key=lambda completo:completo.split()[1])
print(nome.split())
print(nome.split()[1])
