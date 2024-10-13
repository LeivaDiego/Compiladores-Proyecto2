from TypeSystem.object_types import *
from TypeSystem.data_types import *


class Symbol():
    def __init__(self, object: ObjectType):
        self.name = object.id
        self.symbol_type = object.object_type


class SymbolTable():
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, symbol: Symbol):
        self.symbols[symbol.name] = symbol

    def get_symbol(self, name):
        return self.symbols.get(name)

    def __str__(self):
        return str(self.symbols)