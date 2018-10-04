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


if __name__ == '__main__':
    unittest.main()
