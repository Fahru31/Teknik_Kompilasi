import sys
from basiclexer import do_lex
from Parser import do_parse
from Executor import do_calculate

if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(filename)
    characters = file.read()
    file.close()
    tokens = do_lex(characters)
    poliz = do_parse(tokens)
    do_calculate(poliz)