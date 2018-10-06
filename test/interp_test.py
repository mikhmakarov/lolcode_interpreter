import unittest

from lolcodeparse import parse
from lolcodeinterp import LolCodeInterpreter


class InterpreterTest(unittest.TestCase):
    def test_simple_program1(self):
        with open('programs/simple_program1') as f:
            prog = f.read()
            ast = parse(prog)

            inp = LolCodeInterpreter()
            inp.interpret(ast)


if __name__ == '__main__':
    unittest.main()
