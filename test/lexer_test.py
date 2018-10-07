import unittest

from lolcodelex import lexer


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
            assert tokens[14].type == 'AN'

    def test_assignment(self):
        with open('programs/assignment') as f:
            prog = f.read()
            tokens = self.collect_tokens(prog)

            assert len(tokens) == 54
            assert tokens[3].type == 'I'
            assert tokens[4].type == 'HAS'
            assert tokens[5].type == 'A'
            assert tokens[6].type == 'ID'
            assert tokens[20].type == 'GIMMEH'

    def test_switch(self):
        with open('programs/switch') as f:
            prog = f.read()
            tokens = self.collect_tokens(prog)

            assert len(tokens) == 52
            assert tokens[17].type == 'O'
            assert tokens[18].type == 'RLY'
            assert tokens[19].type == 'QUESTION'
            assert tokens[21].type == 'YA'
            assert tokens[22].type == 'RLY'
            assert tokens[30].type == 'MEBBE'


if __name__ == '__main__':
    unittest.main()
