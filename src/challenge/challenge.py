# desafio 1

def inverter (msg):
    return ' '.join(msg.split(' ')[::-1])

# desafio 2

def dma(date):
    l1 = date.split('/')
    l2 = date.split('-')
    if len(l1) == 3:
        return l1
    if len(l2) == 3:
        return l2
    return date
                   
# desafio 3

def anagrama(s1, s2):
    return sorted(s1) == sorted(s2)

print(anagrama('alegria', 'alergia'))
print(anagrama('sim', 'siiimmmmm'))
print(anagrama('palmeiras','abacate'))