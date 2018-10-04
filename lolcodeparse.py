from ply import *

import lolcodelex

tokens = lolcodelex.tokens

VISIBLE = '<VISIBLE>'
GIMMEH = '<GIMMEH>'
SUM = '<SUM>'
DIFF = '<DIFF>'
PRODUKT = '<PRODUKT>'
QUOSHUNT = '<QUOSHUNT>'
MOD = '<MOD>'
BIGGR = '<BIGGR>'
SMALLR = '<SMALLR>'
BOTH = '<BOTH>'
EITHER = '<EITHER>'
WON = '<WON>'
NOT = '<NOT>'
ALL = '<ALL>'
ANY = '<ANY>'
SAME = '<SAME>'
DIFFRINT = '<DIFFRINT>'
SMOOSH = '<SMOOSH>'
MAEK = '<MAEK>'


def p_program(p):
    '''program : HAI FLOAT NEWLINE statements KTHXBYE'''
    p[0] = p[4] if p[4] else []


def p_statements(p):
    '''statements : statements statement
                  | statement'''
    if len(p) == 2:
        p[0] = []
        if p[1]:
            p[0].append(p[1])
    else:
        p[0] = p[1] if p[1] else []

        if p[2]:
            p[0].append(p[2])


def p_statement(p):
    '''statement : command NEWLINE
                 | command COMMA'''
    p[0] = p[1]


def p_command_empty(p):
    '''command : empty'''


def p_command_expr(p):
    '''command : expr'''
    p[0] = p[1]


def p_command_call(p):
    '''command : call'''
    p[0] = p[1]


def p_args(p):
    '''args : args expr
            | expr'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] if p[1] else []

        if p[2]:
            p[0].append(p[2])


def p_sep_args(p):
    '''sep_args : sep_args AN expr
            | expr'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] if p[1] else []

        if p[3]:
            p[0].append(p[3])


def p_type(p):
    '''type : YARN
            | NUMBR
            | NUMBAR
            | NOOB'''
    p[0] = p[1]


def p_call_visible_newline(p):
    '''call : VISIBLE args
            | VISIBLE args EXCLAMATION'''
    newline = len(p) == 3
    p[0] = (VISIBLE, p[2], newline)


def p_call_gimmeh(p):
    '''expr : GIMMEH variable'''
    p[0] = (GIMMEH, p[2])


def p_expr_string(p):
    '''expr : STRING'''
    p[0] = p[1][1:-1]


def p_expr_float(p):
    '''expr : FLOAT'''
    p[0] = float(p[1])


def p_expr_int(p):
    '''expr : INTEGER'''
    p[0] = int(p[1])


def p_expr_bool(p):
    '''expr : WIN
            | FAIL'''
    if p[1] == 'WIN':
        p[0] = True
    elif p[1] == 'FAIL':
        p[0] = False
    else:
        print('unknown bool value', p[1])
        p.parser.error = 1
        return


def p_expr_math(p):
    '''expr : SUM OF expr AN expr
            | DIFF OF expr AN expr
            | PRODUKT OF expr AN expr
            | QUOSHUNT OF expr AN expr
            | MOD OF expr AN expr
            | BIGGR OF expr AN expr
            | SMALLR OF expr AN expr'''
    if p[1] == 'SUM':
        op = SUM
    elif p[1] == 'DIFF':
        op = DIFF
    elif p[1] == 'PRODUKT':
        op = PRODUKT
    elif p[1] == 'QUOSHUNT':
        op = QUOSHUNT
    elif p[1] == 'MOD':
        op = MOD
    elif p[1] == 'BIGGR':
        op = BIGGR
    elif p[1] == 'SMALLR':
        op = SMALLR
    else:
        print('unknown math operator', p[1])
        p.parser.error = 1
        return

    p[0] = (op, [p[3], p[5]])


def p_expr_logic(p):
    '''expr : BOTH OF expr AN expr
            | EITHER OF expr AN expr
            | WON OF expr AN expr
            | NOT expr
            | ALL OF sep_args MKAY
            | ANY OF sep_args MKAY
            | ALL OF args MKAY
            | ANY OF args MKAY'''
    if p[1] == 'BOTH':
        op = BOTH
        p[0] = (op, [p[3], p[5]])
    elif p[1] == 'EITHER':
        op = EITHER
        p[0] = (op, [p[3], p[5]])
    elif p[1] == 'WON':
        op = WON
        p[0] = (op, [p[3], p[5]])
    elif p[1] == 'NOT':
        op = NOT
        p[0] = (op, p[2])
    elif p[1] == 'ALL':
        op = ALL
        p[0] = (op, p[3])
    elif p[1] == 'ANY':
        op = ANY
        p[0] = (op, p[3])
    else:
        print('unknown logic operator', p[1])
        p.parser.error = 1
        return


def p_expr_comp(p):
    '''expr : BOTH SAEM expr AN expr
            | DIFFRINT expr AN expr'''
    if p[1] == 'BOTH':
        p[0] = (SAME, [p[3], p[5]])
    else:
        p[0] = (DIFFRINT, [p[2], p[4]])


def p_expr_concat(p):
    '''expr : SMOOSH sep_args MKAY
            | SMOOSH args MKAY'''
    p[0] = (SMOOSH, p[2])


def p_expr_cast(p):
    '''expr : MAEK expr A type
            | MAEK expr type'''
    if len(p) == 5:
        p[0] = (MAEK, [p[2], p[4]])
    else:
        p[0] = (MAEK, [p[2], p[3]])


def p_variable(p):
    '''variable : ID'''
    p[0] = p[1]


def p_program_error(p):
    '''program : error'''
    p[0] = None
    p.parser.error = 1
    raise Exception('wrong input')


# Empty
def p_empty(p):
    '''empty : '''


# Catastrophic error handler
def p_error(p):
    if not p:
        print("SYNTAX ERROR AT EOF")


bparser = yacc.yacc()


def parse(data):
    bparser.error = 0
    p = bparser.parse(data)
    if bparser.error: return None
    return p
