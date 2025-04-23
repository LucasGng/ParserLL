# Drayan Silva Magalhães, João Vitor Zambão, Lucas Gabriel Nunes Geremias, Lucca Lucchin de Campos Costa 
from consts import *

# Análise Léxica
def is_letra_minuscula(c):
    return 'a' <= c <= 'z'

def is_digito(c):
    return '0' <= c <= '9'

def analisador_lexico_mef(expressao):
    tokens = []
    i = 0
    estado = 'INICIO'

    while i < len(expressao):
        c = expressao[i]

        if estado == 'INICIO':
            if c.isspace():
                i += 1
                continue
            elif c == '(':
                tokens.append(('ABREPAREN', '('))
                i += 1
            elif c == ')':
                tokens.append(('FECHAPAREN', ')'))
                i += 1
            elif c == '\\':
                estado = 'OPERADOR'
                operador = c
                i += 1
            elif c == 't' and expressao[i:i+4] == 'true':
                tokens.append(('CONSTANTE', 'true'))
                i += 4
            elif c == 'f' and expressao[i:i+5] == 'false':
                tokens.append(('CONSTANTE', 'false'))
                i += 5
            elif is_digito(c):
                estado = 'PROPOSICAO'
                prop = c
                i += 1
            else:
                return f"Erro léxico: símbolo inválido '{c}'"

        elif estado == 'OPERADOR':
            while i < len(expressao) and is_letra_minuscula(expressao[i]):
                operador += expressao[i]
                i += 1
            if operador in OPERADORES_UNARIOS:
                tokens.append(('OPERATORUNARIO', operador))
            elif operador in OPERADORES_BINARIOS:
                tokens.append(('OPERATORBINARIO', operador))
            else:
                return f"Erro léxico: operador inválido '{operador}'"
            estado = 'INICIO'

        elif estado == 'PROPOSICAO':
            while i < len(expressao) and (is_digito(expressao[i]) or is_letra_minuscula(expressao[i])):
                prop += expressao[i]
                i += 1
            tokens.append(('PROPOSICAO', prop))
            estado = 'INICIO'

    if estado not in ['INICIO']:
        return "Erro léxico: expressão finalizada em estado inválido"

    return tokens