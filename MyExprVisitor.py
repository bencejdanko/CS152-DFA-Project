from automata.fa.dfa import DFA

from ExprParser import ExprParser
from ExprVisitor import ExprVisitor

class MyExprVisitor(ExprVisitor):

    def __init__(self):
        super(MyExprVisitor, self).__init__()
        self.states = set()
        self.alphabet = set()
        self.dfa = None

    # Visit a parse tree produced by ExprParser#id.
    def visitSym(self, ctx:ExprParser.SymContext):
        return ctx.getText()

    # Visit a parse tree produced by ExprParser#idList.
    def visitSymList(self, ctx:ExprParser.SymListContext):
        sym_list = set()
        ctx_list = ctx.sym()
        for ctx in ctx_list:
            sym_list.add(self.visit(ctx))
        return sym_list
        
    # Visit a parse tree produced by ExprParser#functionItem.
    def visitFunctionItem(self, ctx:ExprParser.FunctionItemContext):
        source = self.visit(ctx.sym()[0])
        symbol = self.visit(ctx.sym()[1])
        destination = self.visit(ctx.sym()[2])
        if source not in self.states:
            raise Exception('Invalid function source state: ' + source)
        if destination not in self.states:
            raise Exception('Invalid function destination state: ' + destination)
        if symbol not in self.alphabet:
            raise Exception('Invalid function symbol: ' + symbol)
        return source, symbol, destination


    # Visit a parse tree produced by ExprParser#functionList.
    def visitFunctionList(self, ctx:ExprParser.FunctionListContext):
        functionList = []
        for ctx in ctx.functionItem():
            source, symbol, destination = self.visit(ctx)
            functionList.append((source, symbol, destination))
        return functionList


    # Visit a parse tree produced by ExprParser#statesSection.
    def visitStatesSection(self, ctx:ExprParser.StatesSectionContext):
        states = self.visit(ctx.symList())
        for state in states:
            self.states.add(state)
        return states

    # Visit a parse tree produced by ExprParser#alphabetSection.
    def visitAlphabetSection(self, ctx:ExprParser.AlphabetSectionContext):
        alphabetList = self.visit(ctx.symList())
        for symbol in alphabetList:
            self.alphabet.add(symbol)
        return alphabetList


    # Visit a parse tree produced by ExprParser#functionSection.
    def visitFunctionSection(self, ctx:ExprParser.FunctionSectionContext):
        functionList = self.visit(ctx.functionList())
        return functionList


    # Visit a parse tree produced by ExprParser#initialSection.
    def visitInitialSection(self, ctx:ExprParser.InitialSectionContext):
        initial = self.visit(ctx.sym())
        if initial not in self.states:
            raise Exception('Invalid initial state: ' + initial)
        return initial


    # Visit a parse tree produced by ExprParser#finalSection.
    def visitFinalSection(self, ctx:ExprParser.FinalSectionContext):
        final = self.visit(ctx.symList())
        for state in final:
            if state not in self.states:
                raise Exception('Invalid final state: ' + state)
        return final


    # Visit a parse tree produced by ExprParser#testSection.
    def visitTestSection(self, ctx:ExprParser.TestSectionContext):
        test = self.visit(ctx.testList())
        return test


    # Visit a parse tree produced by ExprParser#testItem.
    def visitTestItem(self, ctx:ExprParser.TestItemContext):
        sentence = self.visit(ctx.sym()[0])
        result = self.visit(ctx.sym()[1])

        if result == 'accept':
            result = True
        elif result == 'reject':
            result = False
        else:
            raise Exception('Invalid result value: ' + result)
        
        return sentence, result


    # Visit a parse tree produced by ExprParser#testList.
    def visitTestList(self, ctx:ExprParser.TestListContext):
        testList = []
        for ctx in ctx.testItem():
            sentence, result = self.visit(ctx)
            testList.append((sentence, result))
        return testList


    # Visit a parse tree produced by ExprParser#startRule.
    def visitStartRule(self, ctx:ExprParser.StartRuleContext):
        states_section = self.visit(ctx.statesSection())
        alphabet_section = self.visit(ctx.alphabetSection())
        function_section = self.visit(ctx.functionSection())
        initial_section = self.visit(ctx.initialSection())
        final_section = self.visit(ctx.finalSection())
        test_section = self.visit(ctx.testSection())
        
        #validate that each state has a transition for each symbol in alphabet
        track = {}
        for source, symbol, destination in function_section:
            if source not in track:
                track[source] = []
            if symbol not in track[source]:
                track[source].append(symbol)
        for state in states_section:
            print(sorted(track[state]), sorted(alphabet_section))
            if (sorted(track[state]) != sorted(alphabet_section)):
                raise Exception('State ' + state + ' does not have complete transitions.')

        transitions = {}
        for source, symbol, destination in function_section:
            if source not in transitions:
                transitions[source] = {}
            transitions[source][symbol] = destination

        
        dfa = DFA(
            states=states_section,
            input_symbols=alphabet_section,
            transitions=transitions,
            initial_state=initial_section,
            final_states=final_section
        )

        res = 'Validation results:\n'

        for sentence, result in test_section:
            acceptance = dfa.accepts_input(sentence)
            if acceptance != result:
                res += f'{sentence} -> {acceptance} ({result})\n'
            else:
                res += f'{sentence} -> {acceptance}\n'
        return res, dfa