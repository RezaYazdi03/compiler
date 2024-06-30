from antlr4 import *

from grammerListener import grammerListener
from grammerLexer import grammerLexer
from grammerParser import grammerParser

input_expression = input()
lexer = grammerLexer(InputStream(input_expression))
token_stream = CommonTokenStream(lexer)
parser = grammerParser(token_stream)
parse_tree = parser.start()
listener = grammerListener()
walker = ParseTreeWalker()
walker.walk(listener, parse_tree)
result = listener.result
print("Result :", result)
