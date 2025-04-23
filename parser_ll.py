class ParserLL1:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.stack = ['S']  # símbolo inicial da gramática
        self.tabela = {
            ('S', 'CONSTANTE'): ['CONSTANTE'],
            ('S', 'PROPOSICAO'): ['PROPOSICAO'],
            ('S', 'ABREPAREN'): ['ABREPAREN', 'X'],
            ('X', 'CONSTANTE'): ['CONSTANTE'],
            ('X', 'OPERATORUNARIO'): ['UNARIO'],
            ('X', 'OPERATORBINARIO'): ['BINARIO'],
            ('UNARIO', 'OPERATORUNARIO'): ['OPERATORUNARIO', 'S', 'FECHAPAREN'],
            ('BINARIO', 'OPERATORBINARIO'): ['OPERATORBINARIO', 'S', 'S', 'FECHAPAREN'],
        }

    def parser_ll1(self):
        while self.stack:
            topo = self.stack.pop()
            if self.index >= len(self.tokens):
                return "Erro sintático: tokens insuficientes"

            token_atual = self.tokens[self.index]
            token_tipo = token_atual[0]

            if topo in ['CONSTANTE', 'PROPOSICAO', 'ABREPAREN', 'FECHAPAREN', 'OPERATORUNARIO', 'OPERATORBINARIO']:
                if topo == token_tipo:
                    self.index += 1
                else:
                    return f"Erro sintatico: esperado '{topo}', encontrado '{token_tipo}'"
            else:  # topo é um não-terminal
                producao = self.tabela.get((topo, token_tipo))
                if not producao:
                    return f"Erro sintatico: producao indefinida para ({topo}, {token_tipo})"
                self.stack.extend(reversed(producao))  #  empilha da direita pra esquerda

        if self.index != len(self.tokens):
            return "Erro sintático: tokens extras após análise"
        return "Expressão válida!"
