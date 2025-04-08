"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""

def retorna_meio_da_string(a, b):
    meio_a = len(a) // 2
    meio_b = len(b) // 2

    return (meio_a, meio_b)

def front_back(a, b):
    # +++ SUA SOLUÇÃO +++
    if len(a) % 2 == 0:
        if len(b) % 2 == 0:
            meio_string_a, meio_string_b = retorna_meio_da_string(a, b)

            frente_a = a[:meio_string_a]
            tras_a = a[meio_string_a:]

            frente_b = b[:meio_string_b]
            tras_b = b[meio_string_b:]
            resp = f'{frente_a}{frente_b}{tras_a}{tras_b}'
        elif len(b) % 2 != 0:
            meio_string_a, meio_string_b = retorna_meio_da_string(a, b)

            frente_a = a[:meio_string_a]
            tras_a = a[meio_string_a:]

            frente_b = b[:meio_string_b + 1]
            tras_b = b[meio_string_b + 1:]

            resp = f'{frente_a}{frente_b}{tras_a}{tras_b}'
    elif len(a) % 2 != 0 and len(b) % 2 != 0:
        meio_string_a, meio_string_b = retorna_meio_da_string(a, b)

        frente_a = a[:meio_string_a + 1]
        tras_a = a[meio_string_a + 1:]

        frente_b = b[:meio_string_b + 1]
        tras_b = b[meio_string_b + 1:]

        resp = f'{frente_a}{frente_b}{tras_a}{tras_b}'

    return resp


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
