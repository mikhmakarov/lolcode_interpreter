from ply import *

import lolcodelex

tokens = lolcodelex.tokens


def p_program(p):
    '''program : HAI FLOAT statements KTHXBYE'''
    if not p[0]:
        p[0] = []


def p_statements(p):
    '''statements : statements statement
                  | statement'''
    pass


def p_statement(p):
    '''statement : VISIBLE STRING'''
    pass


def p_program_error(p):
    '''program : error'''
    p[0] = None
    p.parser.error = 1




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
