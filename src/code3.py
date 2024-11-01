def prato():
    yield 'arroz'
    # mãe fazendo arroz
    yield 'fejão'
    # pai fazendo feijão
    yield 'bife'
    # fritando o bife

    comida = prato()
    next(comida)

    for x in range (999999999999999999999999999999999999):
        if x == 45:
            print('achei e posso parar')
            break

# clojure
# erlang
# elixir
# Go

# Gil = global interpreter lock