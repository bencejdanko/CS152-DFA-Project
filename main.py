import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyExprVisitor import MyExprVisitor
 

A1 = """
    <states> {q1,q2,q3} 		
    <alphabet> {a,b,c}
    <functions> 
    {
    (q3;a) => q1,
    (q3;b) => q2,
    (q3;c) => q3,

    (q2;a) => q3,
    (q2;b) => q2,
    (q2;c) => q1,

    (q1;a) => q1,
    (q1;b) => q2,
    (q1;c) => q3
    }

    <initial> q3
    <final> {q1} 

    <tests> {
    (a;accept),
    (b;reject),
    (baca;accept),
    (cccccbc;accept)
    }
    """

A2 = """
    <states> {q1,q2} 		
    <alphabet> {a,b}
    <functions> 
    {
    (q1;a) => q1,
    (q1;b) => q2,
    
    (q2;a) => q1,
    (q2;b) => q2
    }

    <initial> q1
    <final> {q2} 

    <tests> {
    (a;accept),
    (b;reject)
    }
    """

def main(argv):
    evaluate(A2)

def evaluate(input_string):
    input = InputStream(input_string)
    lexer = ExprLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.startRule()
    res, dfa = MyExprVisitor().visitStartRule(tree)  # Evaluate the expression
    print(res)
    dfa.show_diagram(path='./diagram.png')

 
 
if __name__ == '__main__':
    main(sys.argv)