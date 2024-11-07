# Aproximação para PI
def pi (n):
    pi = 0
    b = 1
    s = 1
    t = 4
    for i in range (n):
        pi += s*t/b
        s *= -1
        b += 2
    return pi

print(pi(int(input('Enter number: '))))