# Drayan Silva Magalhães, João Vitor Zambão, Lucas Gabriel Nunes Geremias, Lucca Lucchin de Campos Costa 

class ParserError(Exception):
    """Classe base para todas as exceções do parser."""
    pass

class UnexpectedTokenError(ParserError):
    def __init__(self, expected, actual):
        self.expected = expected
        self.actual = actual
        super().__init__(f"Esperado {expected}, mas encontrado {actual}")

class MissingTokenError(ParserError):
    def __init__(self, expected):
        self.expected = expected
        super().__init__(f"Faltando token {expected}")

class InvalidSyntaxError(ParserError):
    def __init__(self, message):
        super().__init__(f"Erro de sintaxe: {message}")