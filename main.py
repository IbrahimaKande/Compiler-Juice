from ply.lex import lex
from ply.yacc import yacc
import lexer
import parser
from os import path
from helper import print_lexer_table

script_dir = path.dirname(__file__)
source_code = path.join(script_dir, 'juice.txt')

f = open(source_code, 'r')

text = f.read()

lexer = lex(module=lexer)
parser = yacc(module=parser, write_tables=False)

expression = parser.parse(text)
print("Tree of the program: ", expression)