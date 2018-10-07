import unittest
import sys
from contextlib import contextmanager
from io import StringIO

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
                assert out.getvalue() == '77lls\nTrueFalse\nFalse\nHELLO'


if __name__ == '__main__':
    unittest.main()
