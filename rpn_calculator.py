import math


class ArithMeticOperatorInterface:
    sign = ''
    
    def update_stack(self, stack):
        last_number = stack.pop()
        before_last_number = stack.pop()
        result = before_last_number + self.sign + last_number
        result = '({})'.format(result)
        stack.append(result)
        return stack


class PythonMathOperatorInterface:
    sign = ''
    
    def update_stack(self, stack):
        last_number = stack.pop()
        result = 'math.{}({})'.format(self.sign, last_number)
        stack.append(result)
        return stack


class SqrtOperator(PythonMathOperatorInterface):
    sign = 'sqrt'


class SineOperator(PythonMathOperatorInterface):
    sign = 'sin'


class Addition(ArithMeticOperatorInterface):
    sign = '+'
        

class Subtraction(ArithMeticOperatorInterface):
    sign = '-'


class Multiplication(ArithMeticOperatorInterface):
    sign = '*'


class Division(ArithMeticOperatorInterface):
    sign = '/'


class Exponentiation(ArithMeticOperatorInterface):
    sign = '^'


class CallOperator:
    operator_object = {
        '+': 'Addition',
        '-': 'Subtraction',
        '*': 'Multiplication',
        '/': 'Division',
        '^': 'Exponentiation',
        'sin': 'SineOperator',
        'sqrt': 'SqrtOperator'
    }

    def create_operator(self, operator):
        targetclass = self.operator_object[operator]
        return globals()[targetclass]()


class RPNCalculator:
    
    def __init__(self):
        self.input_string = ''
        self.string_to_arr = []
        self.rpn_stack = []
        self.result = 0
        
    def calculate_results(self):
        try:
            self.result = eval(self.rpn_stack[0].replace('^', '**'))
        except Exception as e:
            return e
        return self.result

    def calculate(self, input_string):
        self.input_string = input_string
        self.string_to_arr = input_string.split()
        operator = CallOperator()
        
        for item in self.string_to_arr:
            if item in operator.operator_object:
                self.rpn_stack = operator.create_operator(
                    operator=item,
                ).update_stack(self.rpn_stack)
            else:
                self.rpn_stack.append(item)
        return self.rpn_stack[0], self.calculate_results()


if __name__ == '__main__':
    v = input('Please input your RPN string: eg. ("3 sqrt 4 2 * 1 5 - 2 3 ^ ^ / + sin"): ') or '3 sqrt 4 2 * 1 5 - 2 3 ^ ^ / + sin'
    calculator = RPNCalculator()
    rpn_infix, result = calculator.calculate(v)
    print(rpn_infix, ' = ', result)
