import unittest
import sys
from contextlib import contextmanager
from unittest.mock import patch
from io import StringIO

import lolcodeinterp
from lolcodeparse import parse
from lolcodeinterp import LolCodeInterpreter


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class InterpreterTest(unittest.TestCase):
    def test_simple_program1(self):
        with open('programs/simple_program1') as f:
            prog = f.read()
            ast = parse(prog)

            with captured_output() as (out, _):
                inp = LolCodeInterpreter()
                inp.interpret(ast)
                assert out.getvalue() == '77lls\nTrueFalse\nFalse\nHELLO12\n'

    @patch.object(lolcodeinterp, 'input', create=True)
    def test_assignment(self, raw_input):
        with open('programs/assignment') as f:
            prog = f.read()
            ast = parse(prog)
            raw_input.return_value = '10'

            with captured_output() as (out, _):
                inp = LolCodeInterpreter()
                inp.interpret(ast)
                assert out.getvalue() == 'result is 20\n20\n'

    @patch.object(lolcodeinterp, 'input', create=True)
    def test_ifelse(self, raw_input):
        with open('programs/ifelse') as f:
            prog = f.read()
            ast = parse(prog)
            raw_input.return_value = 'mouse'

            with captured_output() as (out, _):
                inp = LolCodeInterpreter()
                inp.interpret(ast)
                assert out.getvalue() == 'Hello mouse\nNice to eat you\n'

    def test_loops(self):
        with open('programs/loops') as f:
            prog = f.read()
            ast = parse(prog)

            with captured_output() as (out, _):
                inp = LolCodeInterpreter()
                inp.interpret(ast)
                assert out.getvalue() == '0 1 2 3 4 5 6 7 8 9 '

    def test_loops2(self):
        with open('programs/loops2') as f:
            prog = f.read()
            ast = parse(prog)

            with captured_output() as (out, _):
                inp = LolCodeInterpreter()
                inp.interpret(ast)
                assert out.getvalue() == '0 2 4 6 8 '


if __name__ == '__main__':
    unittest.main()
