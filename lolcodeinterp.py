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
            node_type, value = statement
            if node_type == EXPR:
                self.process_expr(value)

    def expr_res(self, res):
        self.it = res
        return res

    def process_expr(self, expr):
        node_type, value = expr
        if node_type == VALUE:
            return self.expr_res(self.process_value(value))
        if node_type == VAR:
            return self.expr_res(self.process_variable(value))
        if node_type in [SUM, DIFF, PRODUKT, QUOSHUNT, MOD, BIGGR, SMALLR]:
            return self.expr_res(self.process_binary(node_type, value))

    def process_value(self, val):
        node_type, value = val
        if node_type == YARN:
            return value
        if node_type == NUMBR:
            return int(value)
        if node_type == NUMBAR:
            return float(value)
        if node_type == TROOF:
            if value == WIN:
                return True
            elif value == FAIL:
                return False
            else:
                raise Exception('unknown value for TROOF type')

    def process_variable(self, var_name):
        if var_name == 'IT':
            return self.it

        if var_name in self.vars:
            return self.vars[var_name]

        raise Exception('variable {}: used before declaration'.format(var_name))

    def process_binary(self, op, args):
        lhs = args[0][1]
        rhs = args[1][1]

        if op == SUM:
            return self.process_expr(lhs) + self.process_expr(rhs)
        if op == DIFF:
            return self.process_expr(lhs) - self.process_expr(rhs)
        if op == PRODUKT:
            return self.process_expr(lhs) * self.process_expr(rhs)
        if op == QUOSHUNT:
            return self.process_expr(lhs) / self.process_expr(rhs)
        if op == MOD:
            return self.process_expr(lhs) % self.process_expr(rhs)
        if op == BIGGR:
            return max(self.process_expr(lhs), self.process_expr(rhs))
        if op == SMALLR:
            return min(self.process_expr(lhs), self.process_expr(rhs))

