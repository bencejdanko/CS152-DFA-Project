# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#sym.
    def visitSym(self, ctx:ExprParser.SymContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#symList.
    def visitSymList(self, ctx:ExprParser.SymListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#functionItem.
    def visitFunctionItem(self, ctx:ExprParser.FunctionItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#functionList.
    def visitFunctionList(self, ctx:ExprParser.FunctionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#statesSection.
    def visitStatesSection(self, ctx:ExprParser.StatesSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#alphabetSection.
    def visitAlphabetSection(self, ctx:ExprParser.AlphabetSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#functionSection.
    def visitFunctionSection(self, ctx:ExprParser.FunctionSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#initialSection.
    def visitInitialSection(self, ctx:ExprParser.InitialSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#finalSection.
    def visitFinalSection(self, ctx:ExprParser.FinalSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#testSection.
    def visitTestSection(self, ctx:ExprParser.TestSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#testItem.
    def visitTestItem(self, ctx:ExprParser.TestItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#testList.
    def visitTestList(self, ctx:ExprParser.TestListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#startRule.
    def visitStartRule(self, ctx:ExprParser.StartRuleContext):
        return self.visitChildren(ctx)



del ExprParser