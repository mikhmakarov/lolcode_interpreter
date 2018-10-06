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
            return self.expr_res(self.process_math_expr(node_type, value))
        if node_type in [BOTH, EITHER, WON, NOT, ALL, ANY]:
            return self.expr_res(self.process_logic_expr(node_type, value))

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

    def process_math_expr(self, op, args):
        lhs = self.process_expr(args[0][1])
        rhs = self.process_expr(args[1][1])

        if op == SUM:
            return lhs + rhs
        if op == DIFF:
            return lhs - rhs
        if op == PRODUKT:
            return lhs * rhs
        if op == QUOSHUNT:
            return lhs / rhs
        if op == MOD:
            return lhs % rhs
        if op == BIGGR:
            return max(lhs, rhs)
        if op == SMALLR:
            return min(lhs, rhs)

    def process_logic_expr(self, op, args):
        if op in [BOTH, EITHER, WON]:
            lhs = self.process_expr(args[0][1])
            rhs = self.process_expr(args[1][1])

            if op == BOTH:
                return lhs and rhs
            if op == EITHER:
                return lhs or rhs
            if op == WON:
                return bool(lhs) ^ bool(rhs)
        if op == NOT:
            lhs = self.process_expr(args[1])
            return not lhs
        if op == ALL or op == ANY:
            exprs = [self.process_expr(arg[1]) for arg in args]

            if op == ALL:
                return all(exprs)
            if op == ANY:
                return any(exprs)



