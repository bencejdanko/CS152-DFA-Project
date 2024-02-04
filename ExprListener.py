# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#sym.
    def enterSym(self, ctx:ExprParser.SymContext):
        pass

    # Exit a parse tree produced by ExprParser#sym.
    def exitSym(self, ctx:ExprParser.SymContext):
        pass


    # Enter a parse tree produced by ExprParser#symList.
    def enterSymList(self, ctx:ExprParser.SymListContext):
        pass

    # Exit a parse tree produced by ExprParser#symList.
    def exitSymList(self, ctx:ExprParser.SymListContext):
        pass


    # Enter a parse tree produced by ExprParser#functionItem.
    def enterFunctionItem(self, ctx:ExprParser.FunctionItemContext):
        pass

    # Exit a parse tree produced by ExprParser#functionItem.
    def exitFunctionItem(self, ctx:ExprParser.FunctionItemContext):
        pass


    # Enter a parse tree produced by ExprParser#functionList.
    def enterFunctionList(self, ctx:ExprParser.FunctionListContext):
        pass

    # Exit a parse tree produced by ExprParser#functionList.
    def exitFunctionList(self, ctx:ExprParser.FunctionListContext):
        pass


    # Enter a parse tree produced by ExprParser#statesSection.
    def enterStatesSection(self, ctx:ExprParser.StatesSectionContext):
        pass

    # Exit a parse tree produced by ExprParser#statesSection.
    def exitStatesSection(self, ctx:ExprParser.StatesSectionContext):
        pass


    # Enter a parse tree produced by ExprParser#alphabetSection.
    def enterAlphabetSection(self, ctx:ExprParser.AlphabetSectionContext):
        pass

    # Exit a parse tree produced by ExprParser#alphabetSection.
    def exitAlphabetSection(self, ctx:ExprParser.AlphabetSectionContext):
        pass


    # Enter a parse tree produced by ExprParser#functionSection.
    def enterFunctionSection(self, ctx:ExprParser.FunctionSectionContext):
        pass

    # Exit a parse tree produced by ExprParser#functionSection.
    def exitFunctionSection(self, ctx:ExprParser.FunctionSectionContext):
        pass


    # Enter a parse tree produced by ExprParser#initialSection.
    def enterInitialSection(self, ctx:ExprParser.InitialSectionContext):
        pass

    # Exit a parse tree produced by ExprParser#initialSection.
    def exitInitialSection(self, ctx:ExprParser.InitialSectionContext):
        pass


    # Enter a parse tree produced by ExprParser#finalSection.
    def enterFinalSection(self, ctx:ExprParser.FinalSectionContext):
        pass

    # Exit a parse tree produced by ExprParser#finalSection.
    def exitFinalSection(self, ctx:ExprParser.FinalSectionContext):
        pass


    # Enter a parse tree produced by ExprParser#testSection.
    def enterTestSection(self, ctx:ExprParser.TestSectionContext):
        pass

    # Exit a parse tree produced by ExprParser#testSection.
    def exitTestSection(self, ctx:ExprParser.TestSectionContext):
        pass


    # Enter a parse tree produced by ExprParser#testItem.
    def enterTestItem(self, ctx:ExprParser.TestItemContext):
        pass

    # Exit a parse tree produced by ExprParser#testItem.
    def exitTestItem(self, ctx:ExprParser.TestItemContext):
        pass


    # Enter a parse tree produced by ExprParser#testList.
    def enterTestList(self, ctx:ExprParser.TestListContext):
        pass

    # Exit a parse tree produced by ExprParser#testList.
    def exitTestList(self, ctx:ExprParser.TestListContext):
        pass


    # Enter a parse tree produced by ExprParser#startRule.
    def enterStartRule(self, ctx:ExprParser.StartRuleContext):
        pass

    # Exit a parse tree produced by ExprParser#startRule.
    def exitStartRule(self, ctx:ExprParser.StartRuleContext):
        pass



del ExprParser