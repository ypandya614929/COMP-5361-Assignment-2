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


def is_operator(exp):
    """It takes exp and return boolean based on if it is an operator or not
    Parameters
    ----------
    exp : str
        The str class object

    Returns
    -------
    bool
        return True if exp is in list of operators, False otherwise
    """
    return exp in LIST_OF_OPERATORS


def calculate_conditional(op1, op2):
    """It takes 2 operands and returns their conditional boolean value
    Parameters
    ----------
    op1 : bool
        The bool class object
    op2 : bool
        The bool class object

    Returns
    -------
    bool
        return False if op2 is False, True otherwise
    """
    return not (not op1 and op2)


def calculate_bi_conditional(op1, op2):
    """It takes 2 operands and returns their bi conditional boolean value
    Parameters
    ----------
    op1 : bool
        The bool class object
    op2 : bool
        The bool class object

    Returns
    -------
    bool
        return True if op1 and op2 are same, False otherwise
    """
    return op1 == op2


def calculate_conjunction(op1, op2):
    """It takes 2 operands and returns their conjunction boolean value
    Parameters
    ----------
    op1 : bool
        The bool class object
    op2 : bool
        The bool class object

    Returns
    -------
    bool
        return True if op1 and op2 are True, False otherwise
    """
    return op1 and op2


def calculate_disjunction(op1, op2):
    """It takes 2 operands and returns their disjunction boolean value
    Parameters
    ----------
    op1 : bool
        The bool class object
    op2 : bool
        The bool class object

    Returns
    -------
    bool
        return False if op1 and op2 are False, True otherwise
    """
    return op1 or op2


def calculate_negation(op):
    """It takes one operand and return it's negation boolean value
    Parameters
    ----------
    op : bool
        The bool class object

    Returns
    -------
    bool
        return True if op is False, False if op is True
    """
    return not op


def calculate_ex_or(op1, op2):
    """It takes 2 operands and returns their X-OR boolean value
    Parameters
    ----------
    op1 : bool
        The bool class object
    op2 : bool
        The bool class object

    Returns
    -------
    bool
        return False if op1 and op2 are same, True otherwise
    """
    return not (op1 == op2)


def is_valid_expression(validation_expr_list=[]):
    """It takes list of string/character values from the expression and returns
    boolean value based on the expression is valid or not
    Parameters
    ----------
    validation_expr_list : list
        The list class object

    Returns
    -------
    bool
        return True expression is valid, False otherwise
    """
    parenthesis_count = 0
    operators_count = 0
    last_exp = None
    is_valid = False
    if len(validation_expr_list) > 2:
        for exp in validation_expr_list:
            if exp == "(":
                parenthesis_count += 1
            elif exp == ")":
                parenthesis_count -= 1
                if parenthesis_count < 0:
                    break
            elif is_operator(exp) and (exp not in NEGATION_OPERATORS):
                if last_exp and is_operator(last_exp):
                    if last_exp in NEGATION_OPERATORS:
                        break
                else:
                    operators_count -= 1
            elif not is_operator(exp):
                operators_count += 1
            if operators_count not in [0, 1]:
                break
            last_exp = exp
        if parenthesis_count == 0:
            is_valid = True
    return is_valid


class Equivalency:
    """
    A class used to represent all the calculations for expression evaluation and
    truth table generation

    Attributes
    ----------
    stack : list
        a list which contains the expression data
    postfix_expr_list : list
        a list which contains the expression data in postfix order
    variable_dict : dict
        a dict which contains operand and it's truth values

    Methods
    -------
    __init__()
        It is a general printing method that beautifies print(statement
    push(elem)
    peek()
    pop()
    is_empty()
    is_operand(var)
    check_precedence(op)
    update_variable_dict(key, val)
    get_variable_dict()
    update_postfix_expr_list(expr)
    get_postfix_expr_list()
    generate_expression(expr_list=[])
    evaluate_expression(postfix_expr_list=[])
    calculate_truth_table_and_equivalence()
    """

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
    def is_operand(var):
        if type(var) == bool:
            return True
        if is_operator(var):
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

    def generate_expression(self, expr_list=[]):
        for key in expr_list:
            if key in POSITIVE_VALUES:
                key = True
            if key in NEGATIVE_VALUES:
                key = False
            if self.is_operand(key):
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

    def evaluate_expression(self, postfix_expr_list=[]):
        for exp in postfix_expr_list:
            if self.is_operand(exp):
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
                print('{:<8}'.format(PRINT_VALUE.get(val)), end=' ')
            print('{:<4}'.format('|'), end=' ')
            result = self.evaluate_expression(self.get_postfix_expr_list())
            result_list.append(result)
            print('{:<8}'.format(PRINT_VALUE.get(result)))
        result_set = set(result_list)
        expr_equivalency = "Contingency"
        if len(result_set) == 1:
            expr_equivalency = "Tautology"
            if not result_set.pop():
                expr_equivalency = "Contradiction"
        return expr_equivalency


# python main method
if __name__ == '__main__':

    is_exit = False
    while not is_exit:
        print('\nCOMP-5361 Assignment-2 Menu')
        print("-------------------------------------------------------")
        print('1. Produce output from truth assignments')
        print('2. Display truth table and propositional equivalences')
        print('3. Exit\n')

        choice = input('Select: ')

        choice = choice.strip()
        if choice in ["1", 1, "2", 2]:
            expr = input("\nPlease enter valid propositional logic equation : ")
            for op in LIST_OF_OPERATORS:
                expr = expr.replace(op, " " + op + " ")
            input_expr_list = expr.replace(")", " ) ").replace("(", " ( ").split()
            if not is_valid_expression(input_expr_list):
                print("\n========== Invalid input ==========")
                continue
            print()
            expr_instance = Equivalency()
            expr_instance.generate_expression(input_expr_list)
            updated_expr_list = expr_instance.get_postfix_expr_list()
            calculation_instance = Equivalency()
            calculation_instance.postfix_expr_list = updated_expr_list
            if choice in ["1", 1]:
                for key in sorted(expr_instance.get_variable_dict().keys()):
                    is_valid_input = False
                    while not is_valid_input:
                        val = input("Please enter bool value for {} : ".format(key))
                        val = val.strip()
                        if val in NEGATIVE_VALUES:
                            val = False
                            calculation_instance.update_variable_dict(key, val)
                            is_valid_input = True
                        elif val in POSITIVE_VALUES:
                            val = True
                            calculation_instance.update_variable_dict(key, val)
                            is_valid_input = True
                        else:
                            print("\n========== Invalid input ==========")
                expr_val = calculation_instance.evaluate_expression(updated_expr_list)
                print()
                print("===============================================================================================")
                print("The value of expression {} : {}".format(" ".join(input_expr_list), expr_val))
                print("===============================================================================================")
            elif choice in ["2", 2]:
                print("===============================================================================================")
                for key in sorted(expr_instance.get_variable_dict()):
                    print('{:<8}'.format(key), end=' ')
                print('{:<4}'.format('|'), end=' ')
                print('{:<4}'.format(" ".join(input_expr_list)))
                print("===============================================================================================")
                calculation_instance.variable_dict = expr_instance.get_variable_dict()
                equivalency = calculation_instance.calculate_truth_table_and_equivalence()
                print("===============================================================================================")
                print("Solution : ", equivalency)
                print("===============================================================================================")
        elif choice in ["3", 3]:
            is_exit = True
        else:
            print("\n========== Please select valid option ==========")
