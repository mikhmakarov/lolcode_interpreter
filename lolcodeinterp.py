from constants import *


class LolCodeInterpreter(object):
    def __int__(self, ast):
        self.reset()

    def reset(self):
        self.vars = {}
        self.it = None

    def interpret(self, ast):
        self.reset()
        self.process_statements(ast)

    def process_statements(self, statements):
        for statement in statements:
            node_type, value = statement
            if node_type == EXPR:
                self.process_expr(value)
            if node_type == VISIBLE:
                self.process_visible(value)

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
        if node_type in [SAME, DIFFRINT]:
            return self.expr_res(self.process_equality(node_type, value))
        if node_type == SMOOSH:
            return self.expr_res(self.process_smoosh(value))
        if node_type == MAEK:
            return self.expr_res(self.process_expr_cast(value))

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

    def get_var(self, var_name):
        if var_name in self.vars:
            return self.vars[var_name]

        raise Exception('variable {}: used before declaration'.format(var_name))

    def process_variable(self, var_name):
        if var_name == 'IT':
            return self.it

        return self.get_var(var_name)

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

    def process_equality(self, op, args):
        lhs = self.process_expr(args[0][1])
        rhs = self.process_expr(args[1][1])

        if op == SAME:
            return lhs == rhs
        if op == DIFFRINT:
            return lhs != rhs

    def process_smoosh(self, args):
        str_args = ''.join([str(self.process_expr(arg[1])) for arg in args])
        return str_args

    def process_expr_cast(self, args):
        lhs = self.process_expr(args[0][1])
        t = args[1]

        if t == YARN:
            return str(lhs)
        if t == NUMBR:
            return int(lhs)
        if t == NUMBAR:
            return float(lhs)
        if t == TROOF:
            return bool(lhs)

    def process_visible(self, args):
        to_print, new_line = args
        to_print = ''.join([str(self.process_expr(arg[1])) for arg in to_print])

        print(to_print, end='\n' if new_line else '')

    def process_gimmeh(self, var):
        var_name = var[1]
        # check that variable exists
        self.get_var(var_name)

        self.vars[var_name] = input()
