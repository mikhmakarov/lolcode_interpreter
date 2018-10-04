import unittest

from basiclex import lexer


class LexerTest(unittest.TestCase):
    @staticmethod
    def collect_tokens(prog):
        lexer.input(prog)

        tokens = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            tokens.append(tok)

        return tokens

    def test_hello_world(self):
        with open('programs/hello_world') as f:
            prog = f.read()
            tokens = self.collect_tokens(prog)

            assert len(tokens) == 7
            assert tokens[0].type == 'HAI'
            assert tokens[-1].type == 'KTHXBYE'

    def test_loops(self):
        with open('programs/loops') as f:
            prog = f.read()
            tokens = self.collect_tokens(prog)

            assert len(tokens) == 31
            assert tokens[5].type == 'YR'
            assert tokens[6].type == 'ID'
            assert tokens[7].type == 'UPPIN'
            assert tokens[10].type == 'TIL'
            assert tokens[20].type == 'AN'


if __name__ == '__main__':
    unittest.main()
