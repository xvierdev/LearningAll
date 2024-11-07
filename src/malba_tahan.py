# def malba_tahan():
#     soma = 0
#     for i in range (64):
#         soma += 2**i
#     return soma

def malba_tahan():
    soma = 0
    ant = 1
    for i in range (64):
        soma += ant
        ant *= 2
    return soma

print(malba_tahan())
