from ply import *

keywords = (
    'HAI',              # program start
    'KTHXBYE',          # program end
    'I',                # assignment
    'HAS',              # assignment
    'A',                # assignment
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
    'SAEM',             # equality
    'DIFFRINT',         # inequality
    'AN',               # args separation
    'SMOOSH',           # string concatenation
    'VISIBLE',          # print
    'GIMMEH',           # input
    'O',                # if
    'RLY',              # if
    'YA',               # then
    'NO',               # else
    'WAI',              # else
    'OIC',              # if end
    'MEBBE',            # elseif
    'WTF',              # switch
    'OMG',              # case
    'OMGWTF',           # default
    'GTFO',             # break
    'IM',               # loop
    'IN',               # loop
    'YR',               # loop
    'UPPIN',            # loop increment
    'NERFIN',           # loop decrement
    'OUTTA',            # loop end
    'TIL',              # loop until
    'WILE',             # loop while
    'MAEK',             # cast
    'IS',               # cast
    'NOW'               # cast
)

tokens = keywords + (
    'QUESTION', 'EXCLAMATION', 'COMMA', 'INTEGER', 'FLOAT', 'STRING',
    'ID', 'NEWLINE', 'ELLIPSIS'
)

t_ignore = ' \t\n'


t_QUESTION = r'\?'
t_EXCLAMATION = r'!'
t_COMMA = r'\,'
t_INTEGER = r'\d+'
t_FLOAT = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_STRING = r'\".*\"'
t_ELLIPSIS = r'\.\.\.'


def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t


def t_oneline_comment(t):
    r'BTW .*(\n|\Z)'
    t.lineno += 1


def t_multiline_comment(t):
    r'OBTW(.|\n)*TLDR'
    t.lineno += t.value.count('\n')


def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    if t.value.upper() in keywords:
        t.type = t.value
    return t


def t_error(t):
    print("Illegal character", t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


