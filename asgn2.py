#!/usr/bin/python
# -*- coding: utf-8 -*-

# constants
LIST_OF_OPERATORS = ["¬", "~", "!", "∧", "^", "&", "∨", "v", "|", "V", "=>", "->", "→", "↔", "⊕"]
NEGATION_OPERATORS = ["¬", "~", "!"]
CONJUNCTION_OPERATORS = ["∧", "^", "&"]
DISJUNCTION_OPERATORS = ["∨", "v", "|", "V"]
EX_OR_OPERATORS = ["⊕"]
CONDITIONAL_OPERATORS = ["=>", "->", "→"]
BI_CONDITIONAL_OPERATORS = ["↔"]
PRECEDENCE_MAPPING = {
    "¬": 5, "~": 5, "!": 5,
    "∧": 4, "^": 4, "&": 4,
    "∨": 3,  "v": 3, "|": 3, "V": 3,
    "⊕": 2,
    "=>": 1, "->": 1, "→": 1,
    "↔": 0
}
NEGATIVE_VALUES = ["F", "f", "False", "false", "0", 0]
POSITIVE_VALUES = ["T", "t", "True", "true", "1", 1]
PRINT_VALUE = {
    0: 'False',
    1: 'True'
}


def calculate_conditional(op1, op2):
    return not (not op1 and op2)


def calculate_bi_conditional(op1, op2):
    return op1 == op2


def calculate_conjunction(op1, op2):
    return op1 and op2


def calculate_disjunction(op1, op2):
    return op1 or op2


def calculate_negation(op):
    return not op


def calculate_ex_or(op1, op2):
    return not (op1 == op2)


class Stack:

    def __init__(self):
        self.stack = []
        self.postfix_expr_list = []
        self.variable_dict = {}

    def push(self, elem):
        self.stack.append(elem)

    def peek(self):
        if self.is_empty():
            return 0
        return self.stack[-1]

    def pop(self):
        if self.is_empty():
            return 0
        return self.stack.pop()

    def is_empty(self):
        return self.stack == []

    @staticmethod
    def is_variable(var):
        if type(var) == bool:
            return True
        if var in LIST_OF_OPERATORS:
            return False
        return var.isalnum() or var.isalpha()

    def check_precedence(self, op):
        if self.peek() in ['(']:
            return False
        if (PRECEDENCE_MAPPING[op]) <= PRECEDENCE_MAPPING[self.peek()]:
            return True
        return False

    def update_variable_dict(self, key, val=None):
        self.variable_dict.update({key: val})

    def get_variable_dict(self):
        return self.variable_dict

    def update_postfix_expr_list(self, expr):
        self.postfix_expr_list.append(expr)

    def get_postfix_expr_list(self):
        return self.postfix_expr_list

    def generate_expression(self, expr_list):
        for key in expr_list:
            if key in POSITIVE_VALUES:
                key = True
            if key in NEGATIVE_VALUES:
                key = False
            if self.is_variable(key):
                if type(key) != bool:
                    self.update_variable_dict(key)
                self.update_postfix_expr_list(key)
            elif key == '(':
                self.push(key)
            elif key == ')':
                while not self.is_empty() and self.peek() != '(':
                    self.update_postfix_expr_list(self.pop())
                if not self.is_empty() and self.peek() != '(':
                    return -1
                else:
                    self.pop()
            else:
                while not self.is_empty() and self.check_precedence(key):
                    self.update_postfix_expr_list(self.pop())
                self.push(key)
        while not self.is_empty():
            self.update_postfix_expr_list(self.pop())

    def evaluate_expression(self, postfix_expr_list):
        for exp in postfix_expr_list:
            if self.is_variable(exp):
                if type(exp) != bool:
                    exp = self.get_variable_dict().get(exp)
                self.push(exp)
            else:
                if exp in NEGATION_OPERATORS:
                    op1 = self.pop()
                    self.push(calculate_negation(op1))
                else:
                    op1 = self.pop()
                    op2 = self.pop()
                    if exp in CONJUNCTION_OPERATORS:
                        self.push(calculate_conjunction(op1, op2))
                    elif exp in DISJUNCTION_OPERATORS:
                        self.push(calculate_disjunction(op1, op2))
                    elif exp in EX_OR_OPERATORS:
                        self.push(calculate_ex_or(op1, op2))
                    elif exp in CONDITIONAL_OPERATORS:
                        self.push(calculate_conditional(op1, op2))
                    elif exp in BI_CONDITIONAL_OPERATORS:
                        self.push(calculate_bi_conditional(op1, op2))
        return self.peek()

    def calculate_truth_table_and_equivalence(self):
        variable_list = sorted(self.get_variable_dict().keys())
        table_length = 2 ** len(variable_list)
        result_list = []

        for row_count in range(table_length):
            for var_count, var_name in enumerate(variable_list):
                assign_val = (row_count // (table_length // (2**(var_count+1)))) % 2 == 1
                self.update_variable_dict(var_name, assign_val)
            for key, val in sorted(self.get_variable_dict().items()):
                print('{:<10}'.format(PRINT_VALUE.get(val)), end=' ')
            print('{:<5}'.format('|'), end=' ')
            result = self.evaluate_expression(self.get_postfix_expr_list())
            result_list.append(result)
            print('{:<10}'.format(PRINT_VALUE.get(result)))

        result_set = set(result_list)
        equivalency = "Contingency"
        if len(result_set) == 1:
            equivalency = "Tautology"
            if not result_set.pop():
                equivalency = "Contradiction"
        print("=============================================================================================")
        print("Solution : ", equivalency)


# python main method
if __name__ == '__main__':

    is_exit = False
    while not is_exit:
        print('COMP-5361 Assignment-2 Menu')
        print("-------------------------------------------------------")
        print('1. Produce output from truth assignments')
        print('2. Display truth table and propositional equivalences')
        print('3. Exit')

        choice = input('Select: ')

        choice = choice.strip()
        if choice in ["1", 1, "2", 2]:
            expr = input("Please enter valid propositional logic equation : ")
            for op in LIST_OF_OPERATORS:
                expr = expr.replace(op, " " + op + " ")
            input_expr_list = expr.replace(")", " ) ").replace("(", " ( ").split()
            expr_stack = Stack()
            expr_stack.generate_expression(input_expr_list)
            updated_expr_list = expr_stack.get_postfix_expr_list()
            calculation_stack = Stack()
            calculation_stack.postfix_expr_list = updated_expr_list
            if choice in ["1", 1]:
                for key in sorted(expr_stack.get_variable_dict().keys()):
                    is_valid_input = False
                    while not is_valid_input:
                        val = input("Please enter bool value for {} : ".format(key))
                        val = val.strip()
                        if val in NEGATIVE_VALUES:
                            val = False
                            calculation_stack.update_variable_dict(key, val)
                            is_valid_input = True
                        elif val in POSITIVE_VALUES:
                            val = True
                            calculation_stack.update_variable_dict(key, val)
                            is_valid_input = True
                        else:
                            print("===== Invalid input =====")
                expr_val = calculation_stack.evaluate_expression(updated_expr_list)
                print("=============================================================================================")
                print("The value of expression {} : {}".format(" ".join(input_expr_list), expr_val))
                print("=============================================================================================\n")
            elif choice in ["2", 2]:
                print("=============================================================================================")
                for key in sorted(expr_stack.get_variable_dict()):
                    print('{:<10}'.format(key), end=' ')
                print('{:<5}'.format('|'), end=' ')
                print('{:<5}'.format(" ".join(input_expr_list)))
                print("=============================================================================================")
                calculation_stack.variable_dict = expr_stack.get_variable_dict()
                calculation_stack.calculate_truth_table_and_equivalence()
                print("=============================================================================================\n")
        elif choice in ["3", 3]:
            is_exit = True
        else:
            print("===== Please select valid option =====")
