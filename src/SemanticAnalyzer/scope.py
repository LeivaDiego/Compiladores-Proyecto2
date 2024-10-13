from TypeSystem.object_types import *
from TypeSystem.data_types import *
from symbol import Symbol, SymbolTable


class Scope():
    def __init__(self, parent=None):
        self.parent = parent
        self.symbols = SymbolTable()

    def add_symbol(self, symbol: Symbol):
        self.symbols.add_symbol(symbol)

    def get_symbol(self, name):
        return self.symbols.get_symbol(name)
    

class ScopeManager():
    def __init__(self):
        self.scopes = [Scope()]

    def push_scope(self):
        self.scopes.append(Scope(self.scopes[-1]))

    def pop_scope(self):
        self.scopes.pop()

    def add_symbol(self, symbol: Symbol):
        self.scopes[-1].add_symbol(symbol)

    def get_symbol(self, name):
        for scope in reversed(self.scopes):
            symbol = scope.get_symbol(name)
            if symbol:
                return symbol
        return None