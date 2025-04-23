# Drayan Silva Magalhães, João Vitor Zambão, Lucas Gabriel Nunes Geremias, Lucca Lucchin de Campos Costa 

# Parser LL(1) baseado em tokens do analisador léxico
from errors import *

class Parser:
    def __init__(self):
        self.tokens = None
        self.pos = 0

    def clear(self) -> None:
        self.tokens = None
        self.pos = 0

    def token_atual(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consumir(self, tipo_esperado=None):
        token = self.token_atual()
        if token is None:
            if tipo_esperado is not None:
                raise MissingTokenError(tipo_esperado)
            else:
                raise MissingTokenError("qualquer token")
        if tipo_esperado is not None and token[0] != tipo_esperado:
            raise UnexpectedTokenError(tipo_esperado, token[0])
        self.pos += 1
        return token

    def parse(self, tokens:list):
        try:
            self.tokens = tokens
            self.formula()
            if self.token_atual() is not None:
                curr_token = self.token_atual()[0]
                self.clear()
                raise UnexpectedTokenError("fim da entrada", curr_token)
            self.clear()
            return "valida"
        except ParserError:
            self.clear()
            return "inválida"

    def formula(self):
        token = self.token_atual()
        if token is None:
            raise InvalidSyntaxError("Fórmula incompleta")
        if token[0] == 'CONSTANTE':
            self.consumir('CONSTANTE')
        elif token[0] == 'PROPOSICAO':
            self.consumir('PROPOSICAO')
        elif token[0] == 'ABREPAREN':
            self.formula_unaria_ou_binaria()
        else:
            raise UnexpectedTokenError("CONSTANTE, PROPOSICAO ou ABREPAREN", token[0])
        return True

    def formula_unaria_ou_binaria(self):
        self.consumir('ABREPAREN')
        token = self.token_atual()
        if token is None:
            raise MissingTokenError("OPERATORUNARIO ou OPERATORBINARIO")
        if token[0] == 'OPERATORUNARIO':
            self.consumir('OPERATORUNARIO')
            self.formula()
            self.consumir('FECHAPAREN')
        elif token[0] == 'OPERATORBINARIO':
            self.consumir('OPERATORBINARIO')
            self.formula()
            self.formula()
            self.consumir('FECHAPAREN')
        else:
            print("OPERATORUNARIO ou OPERATORBINARIO")
            raise UnexpectedTokenError("OPERATORUNARIO ou OPERATORBINARIO", token[0])
        return True