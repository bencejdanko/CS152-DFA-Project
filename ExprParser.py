# Generated from Expr.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,15,102,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,1,1,1,1,1,5,1,32,8,1,10,1,12,1,35,9,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,5,3,48,8,3,10,3,12,3,51,9,3,1,4,1,4,1,4,1,4,
        1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,
        1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,
        11,1,11,1,11,5,11,90,8,11,10,11,12,11,93,9,11,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,0,
        91,0,26,1,0,0,0,2,28,1,0,0,0,4,36,1,0,0,0,6,44,1,0,0,0,8,52,1,0,
        0,0,10,57,1,0,0,0,12,62,1,0,0,0,14,67,1,0,0,0,16,70,1,0,0,0,18,75,
        1,0,0,0,20,80,1,0,0,0,22,86,1,0,0,0,24,94,1,0,0,0,26,27,5,14,0,0,
        27,1,1,0,0,0,28,33,3,0,0,0,29,30,5,1,0,0,30,32,3,0,0,0,31,29,1,0,
        0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,3,1,0,0,0,35,33,
        1,0,0,0,36,37,5,2,0,0,37,38,3,0,0,0,38,39,5,3,0,0,39,40,3,0,0,0,
        40,41,5,4,0,0,41,42,5,5,0,0,42,43,3,0,0,0,43,5,1,0,0,0,44,49,3,4,
        2,0,45,46,5,1,0,0,46,48,3,4,2,0,47,45,1,0,0,0,48,51,1,0,0,0,49,47,
        1,0,0,0,49,50,1,0,0,0,50,7,1,0,0,0,51,49,1,0,0,0,52,53,5,6,0,0,53,
        54,5,7,0,0,54,55,3,2,1,0,55,56,5,8,0,0,56,9,1,0,0,0,57,58,5,9,0,
        0,58,59,5,7,0,0,59,60,3,2,1,0,60,61,5,8,0,0,61,11,1,0,0,0,62,63,
        5,10,0,0,63,64,5,7,0,0,64,65,3,6,3,0,65,66,5,8,0,0,66,13,1,0,0,0,
        67,68,5,11,0,0,68,69,3,0,0,0,69,15,1,0,0,0,70,71,5,12,0,0,71,72,
        5,7,0,0,72,73,3,2,1,0,73,74,5,8,0,0,74,17,1,0,0,0,75,76,5,13,0,0,
        76,77,5,7,0,0,77,78,3,22,11,0,78,79,5,8,0,0,79,19,1,0,0,0,80,81,
        5,2,0,0,81,82,3,0,0,0,82,83,5,3,0,0,83,84,3,0,0,0,84,85,5,4,0,0,
        85,21,1,0,0,0,86,91,3,20,10,0,87,88,5,1,0,0,88,90,3,20,10,0,89,87,
        1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,23,1,0,0,0,
        93,91,1,0,0,0,94,95,3,8,4,0,95,96,3,10,5,0,96,97,3,12,6,0,97,98,
        3,14,7,0,98,99,3,16,8,0,99,100,3,18,9,0,100,25,1,0,0,0,3,33,49,91
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'('", "';'", "')'", "'=>'", "'<states>'", 
                     "'{'", "'}'", "'<alphabet>'", "'<functions>'", "'<initial>'", 
                     "'<final>'", "'<tests>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SYM", "WS" ]

    RULE_sym = 0
    RULE_symList = 1
    RULE_functionItem = 2
    RULE_functionList = 3
    RULE_statesSection = 4
    RULE_alphabetSection = 5
    RULE_functionSection = 6
    RULE_initialSection = 7
    RULE_finalSection = 8
    RULE_testSection = 9
    RULE_testItem = 10
    RULE_testList = 11
    RULE_startRule = 12

    ruleNames =  [ "sym", "symList", "functionItem", "functionList", "statesSection", 
                   "alphabetSection", "functionSection", "initialSection", 
                   "finalSection", "testSection", "testItem", "testList", 
                   "startRule" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    SYM=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SymContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYM(self):
            return self.getToken(ExprParser.SYM, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_sym

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSym" ):
                listener.enterSym(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSym" ):
                listener.exitSym(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSym" ):
                return visitor.visitSym(self)
            else:
                return visitor.visitChildren(self)




    def sym(self):

        localctx = ExprParser.SymContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sym)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(ExprParser.SYM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SymListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sym(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.SymContext)
            else:
                return self.getTypedRuleContext(ExprParser.SymContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_symList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSymList" ):
                listener.enterSymList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSymList" ):
                listener.exitSymList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSymList" ):
                return visitor.visitSymList(self)
            else:
                return visitor.visitChildren(self)




    def symList(self):

        localctx = ExprParser.SymListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_symList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.sym()
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 29
                self.match(ExprParser.T__0)
                self.state = 30
                self.sym()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sym(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.SymContext)
            else:
                return self.getTypedRuleContext(ExprParser.SymContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_functionItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionItem" ):
                listener.enterFunctionItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionItem" ):
                listener.exitFunctionItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionItem" ):
                return visitor.visitFunctionItem(self)
            else:
                return visitor.visitChildren(self)




    def functionItem(self):

        localctx = ExprParser.FunctionItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_functionItem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(ExprParser.T__1)
            self.state = 37
            self.sym()
            self.state = 38
            self.match(ExprParser.T__2)
            self.state = 39
            self.sym()
            self.state = 40
            self.match(ExprParser.T__3)
            self.state = 41
            self.match(ExprParser.T__4)
            self.state = 42
            self.sym()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.FunctionItemContext)
            else:
                return self.getTypedRuleContext(ExprParser.FunctionItemContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_functionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionList" ):
                listener.enterFunctionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionList" ):
                listener.exitFunctionList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionList" ):
                return visitor.visitFunctionList(self)
            else:
                return visitor.visitChildren(self)




    def functionList(self):

        localctx = ExprParser.FunctionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_functionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.functionItem()
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 45
                self.match(ExprParser.T__0)
                self.state = 46
                self.functionItem()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatesSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def symList(self):
            return self.getTypedRuleContext(ExprParser.SymListContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_statesSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatesSection" ):
                listener.enterStatesSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatesSection" ):
                listener.exitStatesSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatesSection" ):
                return visitor.visitStatesSection(self)
            else:
                return visitor.visitChildren(self)




    def statesSection(self):

        localctx = ExprParser.StatesSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statesSection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(ExprParser.T__5)
            self.state = 53
            self.match(ExprParser.T__6)
            self.state = 54
            self.symList()
            self.state = 55
            self.match(ExprParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlphabetSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def symList(self):
            return self.getTypedRuleContext(ExprParser.SymListContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_alphabetSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlphabetSection" ):
                listener.enterAlphabetSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlphabetSection" ):
                listener.exitAlphabetSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlphabetSection" ):
                return visitor.visitAlphabetSection(self)
            else:
                return visitor.visitChildren(self)




    def alphabetSection(self):

        localctx = ExprParser.AlphabetSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_alphabetSection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(ExprParser.T__8)
            self.state = 58
            self.match(ExprParser.T__6)
            self.state = 59
            self.symList()
            self.state = 60
            self.match(ExprParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionList(self):
            return self.getTypedRuleContext(ExprParser.FunctionListContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_functionSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionSection" ):
                listener.enterFunctionSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionSection" ):
                listener.exitFunctionSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionSection" ):
                return visitor.visitFunctionSection(self)
            else:
                return visitor.visitChildren(self)




    def functionSection(self):

        localctx = ExprParser.FunctionSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functionSection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(ExprParser.T__9)
            self.state = 63
            self.match(ExprParser.T__6)
            self.state = 64
            self.functionList()
            self.state = 65
            self.match(ExprParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitialSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sym(self):
            return self.getTypedRuleContext(ExprParser.SymContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_initialSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitialSection" ):
                listener.enterInitialSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitialSection" ):
                listener.exitInitialSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitialSection" ):
                return visitor.visitInitialSection(self)
            else:
                return visitor.visitChildren(self)




    def initialSection(self):

        localctx = ExprParser.InitialSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_initialSection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(ExprParser.T__10)
            self.state = 68
            self.sym()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FinalSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def symList(self):
            return self.getTypedRuleContext(ExprParser.SymListContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_finalSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinalSection" ):
                listener.enterFinalSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinalSection" ):
                listener.exitFinalSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFinalSection" ):
                return visitor.visitFinalSection(self)
            else:
                return visitor.visitChildren(self)




    def finalSection(self):

        localctx = ExprParser.FinalSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_finalSection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(ExprParser.T__11)
            self.state = 71
            self.match(ExprParser.T__6)
            self.state = 72
            self.symList()
            self.state = 73
            self.match(ExprParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TestSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def testList(self):
            return self.getTypedRuleContext(ExprParser.TestListContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_testSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTestSection" ):
                listener.enterTestSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTestSection" ):
                listener.exitTestSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTestSection" ):
                return visitor.visitTestSection(self)
            else:
                return visitor.visitChildren(self)




    def testSection(self):

        localctx = ExprParser.TestSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_testSection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(ExprParser.T__12)
            self.state = 76
            self.match(ExprParser.T__6)
            self.state = 77
            self.testList()
            self.state = 78
            self.match(ExprParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TestItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sym(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.SymContext)
            else:
                return self.getTypedRuleContext(ExprParser.SymContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_testItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTestItem" ):
                listener.enterTestItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTestItem" ):
                listener.exitTestItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTestItem" ):
                return visitor.visitTestItem(self)
            else:
                return visitor.visitChildren(self)




    def testItem(self):

        localctx = ExprParser.TestItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_testItem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(ExprParser.T__1)
            self.state = 81
            self.sym()
            self.state = 82
            self.match(ExprParser.T__2)
            self.state = 83
            self.sym()
            self.state = 84
            self.match(ExprParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TestListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def testItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.TestItemContext)
            else:
                return self.getTypedRuleContext(ExprParser.TestItemContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_testList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTestList" ):
                listener.enterTestList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTestList" ):
                listener.exitTestList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTestList" ):
                return visitor.visitTestList(self)
            else:
                return visitor.visitChildren(self)




    def testList(self):

        localctx = ExprParser.TestListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_testList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.testItem()
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 87
                self.match(ExprParser.T__0)
                self.state = 88
                self.testItem()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StartRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statesSection(self):
            return self.getTypedRuleContext(ExprParser.StatesSectionContext,0)


        def alphabetSection(self):
            return self.getTypedRuleContext(ExprParser.AlphabetSectionContext,0)


        def functionSection(self):
            return self.getTypedRuleContext(ExprParser.FunctionSectionContext,0)


        def initialSection(self):
            return self.getTypedRuleContext(ExprParser.InitialSectionContext,0)


        def finalSection(self):
            return self.getTypedRuleContext(ExprParser.FinalSectionContext,0)


        def testSection(self):
            return self.getTypedRuleContext(ExprParser.TestSectionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_startRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStartRule" ):
                listener.enterStartRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStartRule" ):
                listener.exitStartRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStartRule" ):
                return visitor.visitStartRule(self)
            else:
                return visitor.visitChildren(self)




    def startRule(self):

        localctx = ExprParser.StartRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_startRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.statesSection()
            self.state = 95
            self.alphabetSection()
            self.state = 96
            self.functionSection()
            self.state = 97
            self.initialSection()
            self.state = 98
            self.finalSection()
            self.state = 99
            self.testSection()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





