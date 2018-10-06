import unittest

from lolcodeparse import parse
from constants import *


class ParserTest(unittest.TestCase):
    def test_hello_world(self):
        with open('programs/hello_world') as f:
            prog = f.read()
            ast = parse(prog)

            assert len(ast) == 1
            assert ast[0][0] == VISIBLE
            assert ast[0][1][0][1] == (VALUE, (YARN, 'Hai world!'))

    def test_expr(self):
        with open('programs/expr') as f:
            prog = f.read()
            ast = parse(prog)

            assert len(ast) == 3
            assert ast[0][0] == VISIBLE
            assert ast[0][1][0][1] == (VALUE, (YARN, 'Hai world!'))
            assert ast[0][1][2][1][0] == SUM
            assert ast[0][1][3][1][0] == BOTH
            assert ast[0][1][3][1][1][0][1] == (VALUE, (TROOF, 'WIN'))
            assert ast[0][1][3][1][1][1][1] == (VALUE, (TROOF, 'FAIL'))
            assert ast[0][1][4][1][0] == ALL
            assert ast[1][1][0][1][0] == SAME
            assert ast[1][1][1][1][0] == MAEK
            assert ast[1][1][1][1][1][-1] == NUMBR
            assert ast[2][0] == GIMMEH

    def test_assignment(self):
        with open('programs/assignment') as f:
            prog = f.read()
            ast = parse(prog)

            assert len(ast) == 9
            assert ast[0][0] == DECLARE
            assert ast[0][1][0][0] == VAR
            assert ast[0][1][0][1] == 'x'
            assert ast[0][1][1] is None
            assert ast[2][1][1][1][1] == '0'
            assert ast[6][0] == CAST
            assert ast[6][1][0][0] == VAR
            assert ast[6][1][0][1] == 'y'
            assert ast[6][1][1] == NUMBR

    def test_if_else(self):
        with open('programs/ifelse') as f:
            prog = f.read()
            ast = parse(prog)

            assert len(ast) == 4
            assert ast[3][0] == IF_ELSE
            assert ast[3][1][0][0] == VISIBLE
            assert ast[3][1][1][0] == VISIBLE

    def test_loop(self):
        with open('programs/loops') as f:
            prog = f.read()
            ast = parse(prog)

            assert len(ast) == 1
            assert ast[0][0] == LOOP
            assert ast[0][1][0][0] == VAR
            assert ast[0][1][2][0] == TIL
            assert ast[0][1][2][1][1][0] == SAME
            assert ast[0][1][3][0][0] == VISIBLE


if __name__ == '__main__':
    unittest.main()
