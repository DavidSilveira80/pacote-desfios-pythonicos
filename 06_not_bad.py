"""
06. not_bad

Dada uma string, encontre a primeira aparição das
substrings 'not' e 'bad'. Se 'bad' aparecer depois
de 'not', troque todo o trecho entre 'not' e 'bad'
por 'good' e retorne a string resultante.

Exemplo: 'The dinner is not that bad!' retorna 'The dinner is good!'
"""
def verivica_antes_depois_da_palavra(sentenca, indice_palavra):
    verificado_antes_depois = (True if sentenca[indice_palavra - 1] == ' ' or
                                       sentenca[indice_palavra - 1] == ''  and
                                       sentenca[indice_palavra + 3] == ' ' or
                                       sentenca[indice_palavra + 3] == '!' or
                                       sentenca[indice_palavra + 3] == '.'
                                       else False)
    return verificado_antes_depois


def meu_regex(s):
    indice_not = s.index('not')
    indice_bad = s.index('bad')

    he_not = verivica_antes_depois_da_palavra(s, indice_not)

    he_bad = verivica_antes_depois_da_palavra(s, indice_bad)

    return he_not and he_bad

def not_bad(s):
    # +++ SUA SOLUÇÃO +++
    if ('bad' in s and 'not' in s):
        indice_not = s.index('not')
        indice_bad = s.index('bad')

        if (indice_bad > indice_not) and (meu_regex(s)):
            resp = s.replace(s[indice_not: indice_bad + 3], 'good')
        else:
            resp = s
    elif 'not' not in s or 'bad' not in s:
        resp = s
    return resp


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(not_bad, 'This movie is not so bad', 'This movie is good')
    test(not_bad, 'This dinner is not that bad!', 'This dinner is good!')
    test(not_bad, 'This tea is not hot', 'This tea is not hot')
    test(not_bad, "It's bad yet not", "It's bad yet not")
