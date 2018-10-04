from ply import *

keywords = (
    'BTW'               # one line comment
    'OBTW',             # multi line comment start
    'TLDR',             # multi line comment end
    'HAI',              # program start
    'KTHXBYE',          # program end
    'I HAS A',          # assignment
    'ITZ',              # assignment
    'R',                # assignment
    'YARN',             # string type
    'NUMBR',            # integer type
    'NUMBAR',           # float type
    'TROOF',            # boolean type
    'BUKKIT',           # array type
    'NOOB',             # untyped
    'WIN',              # true
    'FAIL',             # false
    'MKAY',             # for operators with variable arity
    'OF',               # for math operations
    'SUM',              # +
    'DIFF',             # -
    'PRODUKT',          # *
    'QUOSHUNT',         # /
    'MOD',              # modulo
    'BIGGR',            # max
    'SMALLR',           # min
    'BOTH',             # logical and
    'EITHER',           # logical or
    'WON',              # logical xor,
    'NOT',              # logical not
    'ANY',              # true if any of args are true
    'ALL',              # true if all args are true
    'SMOOSH',           # string concatenation
    'VISIBLE',          # print
    'GIMMEH',           # input
    'O RLY?',           # if
    'YA RLY',           # then
    'NO WAI',           # else
    'OIC',              # if end
    'MEBBE',            # elseif
    'WTF?',             # switch
    'OMG',              # case
    'OMGWTF',           # default
    'GTFO',             # break
    'IM IN YR',         # for loop
    'IM OUTTA YR',      # for loop end
    'YR',               # loop iterator
    'TIL',              # loop until
    'WILE'              # loop while
)

tokens = keywords + (
    'COMMA', 'INTEGER', 'FLOAT', 'STRING',
    'ID', 'NEWLINE'
)

t_ignore = ' \t'


t_COMMA = r'\,'
t_INTEGER = r'\d+'
t_FLOAT = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_STRING = r'\".*?\"'


def t_ID(t):
    """[A-Z][A-Z0-9]"""
    if t.value in keywords:
        t.type = t.value
    return t


def t_NEWLINE(t):
    """\n"""
    t.lexer.lineno += 1
    return t


def t_error(t):
    print("Illegal character", t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


