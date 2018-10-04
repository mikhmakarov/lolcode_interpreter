import unittest

from lolcodeparse import parse


class ParserTest(unittest.TestCase):
    def test_hello_world(self):
        with open('programs/hello_world') as f:
            prog = f.read()
            parse(prog)


if __name__ == '__main__':
    unittest.main()
