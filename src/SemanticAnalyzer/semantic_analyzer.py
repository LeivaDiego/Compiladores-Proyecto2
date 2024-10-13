from CompiScript.compiscriptVisitor import compiscriptVisitor
from CompiScript.compiscriptParser import compiscriptParser
from TypeSystem.object_types import *
from TypeSystem.data_types import *

class SemanticAnalyzer(compiscriptVisitor):
    def __init__(self):
        self.current_class = None
        self.current_function = None
        self.current_variable = None

    def visitProgram(self, ctx:compiscriptParser.ProgramContext):
        print("Entered Program")
        return self.visitChildren(ctx)


    def visitDeclaration(self, ctx:compiscriptParser.DeclarationContext):
        print("Entered Declaration")
        return self.visitChildren(ctx)


    def visitClassDecl(self, ctx:compiscriptParser.ClassDeclContext):
        print("Entered Class Declaration")
        return self.visitChildren(ctx)


    def visitFunDecl(self, ctx:compiscriptParser.FunDeclContext):
        print("Entered Function Declaration")
        return self.visitChildren(ctx)


    def visitVarDecl(self, ctx:compiscriptParser.VarDeclContext):
        print("Entered Variable Declaration")
        return self.visitChildren(ctx)


    def visitStatement(self, ctx:compiscriptParser.StatementContext):
        print("Entered Statement")
        return self.visitChildren(ctx)


    def visitExprStmt(self, ctx:compiscriptParser.ExprStmtContext):
        print("Entered Expression Statement")
        return self.visitChildren(ctx)


    def visitForStmt(self, ctx:compiscriptParser.ForStmtContext):
        print("Entered For Statement")
        return self.visitChildren(ctx)


    def visitIfStmt(self, ctx:compiscriptParser.IfStmtContext):
        print("Entered If Statement")
        return self.visitChildren(ctx)


    def visitPrintStmt(self, ctx:compiscriptParser.PrintStmtContext):
        print("Entered Print Statement")
        return self.visitChildren(ctx)


    def visitReturnStmt(self, ctx:compiscriptParser.ReturnStmtContext):
        print("Entered Return Statement")
        return self.visitChildren(ctx)


    def visitWhileStmt(self, ctx:compiscriptParser.WhileStmtContext):
        print("Entered While Statement")
        return self.visitChildren(ctx)


    def visitBlock(self, ctx:compiscriptParser.BlockContext):
        print("Entered Block")
        return self.visitChildren(ctx)


    def visitFunAnon(self, ctx:compiscriptParser.FunAnonContext):
        print("Entered Anonymous Function")
        return self.visitChildren(ctx)


    def visitExpression(self, ctx:compiscriptParser.ExpressionContext):
        print("Entered Expression")
        return self.visitChildren(ctx)


    def visitAssignment(self, ctx:compiscriptParser.AssignmentContext):
        print("Entered Assignment")
        return self.visitChildren(ctx)


    def visitLogic_or(self, ctx:compiscriptParser.Logic_orContext):
        print("Entered Logic Or")
        return self.visitChildren(ctx)


    def visitLogic_and(self, ctx:compiscriptParser.Logic_andContext):
        print("Entered Logic And")
        return self.visitChildren(ctx)


    def visitEquality(self, ctx:compiscriptParser.EqualityContext):
        print("Entered Equality")
        return self.visitChildren(ctx)


    def visitComparison(self, ctx:compiscriptParser.ComparisonContext):
        print("Entered Comparison")
        return self.visitChildren(ctx)


    def visitTerm(self, ctx:compiscriptParser.TermContext):
        print("Entered Term")
        return self.visitChildren(ctx)


    def visitFactor(self, ctx:compiscriptParser.FactorContext):
        print("Entered Factor")
        return self.visitChildren(ctx)


    def visitArray(self, ctx:compiscriptParser.ArrayContext):
        print("Entered Array")
        return self.visitChildren(ctx)


    def visitInstantiation(self, ctx:compiscriptParser.InstantiationContext):
        print("Entered Instantiation")
        return self.visitChildren(ctx)


    def visitUnary(self, ctx:compiscriptParser.UnaryContext):
        print("Entered Unary")
        return self.visitChildren(ctx)


    def visitCall(self, ctx:compiscriptParser.CallContext):
        print("Entered Call")
        return self.visitChildren(ctx)


    def visitPrimary(self, ctx:compiscriptParser.PrimaryContext):
        print("Entered Primary")
        return self.visitChildren(ctx)


    def visitFunction(self, ctx:compiscriptParser.FunctionContext):
        print("Entered Function")
        return self.visitChildren(ctx)


    def visitParameters(self, ctx:compiscriptParser.ParametersContext):
        print("Entered Parameters")
        return self.visitChildren(ctx)


    def visitArguments(self, ctx:compiscriptParser.ArgumentsContext):
        print("Entered Arguments")
        return self.visitChildren(ctx)