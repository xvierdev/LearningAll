def inverte(frase). Faça uma função que recebva uma frase como entrada, e devolva as palavras da frase invertidas.
inverte('batatinha quando nasce') -> 'nasce quando batatinha'

def dma(s). Existem datas em dois formatos: 'dd-mm-aaaa', 'dd/mm/aaaa'. Retorne dia, mês e ano numa lista. Se não houver '-' ou '/' retorne a string original.
dma('08-11-2024') -> ['08', '11', '2024']
dma('08/11/2024') -> ['08', '11', '2024']
dma('abobrinha') -> 'abobrinha'

def anagrama (s1, s2). Duas palavras são anagramas quando possuem as mesmas letra em outra ordem. Sem usar repetições (for e while).
anagrama('alegria', 'alergia') -> True
anagrama('sim', 'siiimmmmm') -> False
anagrama('palmeiras', 'abacate') -> False