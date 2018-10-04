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

            assert len(tokens) == 5
            assert tokens[0].type == 'HAI'
            assert tokens[-1].type == 'KTHXBYE'

    def test_loops(self):
        with open('programs/loops') as f:
            prog = f.read()
            tokens = self.collect_tokens(prog)

            assert len(tokens) == 27
            assert tokens[4].type == 'YR'
            assert tokens[5].type == 'ID'
            assert tokens[6].type == 'UPPIN'
            assert tokens[9].type == 'TIL'
            assert tokens[13].type == 'AN'

    def test_assignment(self):
        with open('programs/assignment') as f:
            prog = f.read()
            tokens = self.collect_tokens(prog)

            assert len(tokens) == 38
            assert tokens[2].type == 'I'
            assert tokens[3].type == 'HAS'
            assert tokens[4].type == 'A'
            assert tokens[5].type == 'ID'
            assert tokens[14].type == 'GIMMEH'


if __name__ == '__main__':
    unittest.main()
