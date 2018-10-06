from constants import *


class LolCodeInterpreter(object):
    def __int__(self, ast):
        self.reset()

    def reset(self):
        self.vars = {}
        self.it = None

    def interpret(self, ast):
        self.reset()

        try:
            # top level is a list of statements
            self.process_statements(ast)
        except Exception as e:
            print('unable to interpret program ', e)

    def process_statements(self, statements):
        for statement in statements:
            if statement[0] == EXPR:
                self.process_expr(statement[1])

    def expr_res(self, res):
        self.it = res
        return res

    def process_expr(self, expr):
        node_type, value = expr
        if node_type == VALUE:
            return self.expr_res(self.process_value(value))
        if node_type == VAR:
            return self.expr_res(self.process_variable(value))


    def process_value(self, val):
        if val[0] == YARN:
            return val[1]
        elif val[0] == NUMBR:
            return int(val[1])
        elif val[0] == NUMBAR:
            return float(val[1])
        elif val[0] == TROOF:
            if val[1] == WIN:
                return True
            elif val[1] == FAIL:
                return False
            else:
                raise Exception('unknown value for TROOF type')

    def process_variable(self, var_name):
        if var_name == 'IT':
            return self.it

        if var_name in self.vars:
            return self.vars[var_name]

        raise Exception('variable {}: used before declaration'.format(var_name))

