grammar Expr;
SYM : [a-zA-Z0-9]+ ;
sym : SYM ;
symList: sym (',' sym)* ;

functionItem: '(' sym ';' sym ')' '=>' sym ;
functionList: functionItem (',' functionItem)* ;

statesSection: '<states>' '{' symList '}' ;
alphabetSection: '<alphabet>' '{' symList '}' ;
functionSection: '<functions>' '{' functionList '}' ;
initialSection: '<initial>'  sym ;
finalSection: '<final>' '{' symList '}' ;
testSection: '<tests>' '{' testList '}' ;

testItem: '(' sym ';' sym ')' ;
testList: testItem (',' testItem)* ;

startRule: statesSection alphabetSection functionSection initialSection finalSection testSection;

WS      : [ \t\r\n]+ -> channel(HIDDEN) ;

// source ~/venv/bin/activate
// antlr4 -Dlanguage=Python3 -visitor Expr.g4