class PredictiveParser:
    def __init__(self):
        self.parsing_table = {
            'S': {'a': 'aW', '=': '', '+': '', '-': '', '/': '', '*': '', '(': '', ')': '', '$': ''},
            'W': {'a': '', '=': '=E', '+': '', '-': '', '/': '', '*': '', '(': '', ')': '', '$': ''},
            'E': {'a': 'TQ', '=': '', '+': '', '-': '', '/': '', '*': '', '(': 'TQ', ')': '', '$': ''},
            'Q': {'a': '', '=': '', '+': '+TQ', '-': '-TQ', '/': '', '*': '', '(': '', ')': 'lambda', '$': 'lambda'},
            'T': {'a': 'FR', '=': '', '+': '', '-': '', '/': '', '*': '', '(': 'FR', ')': '', '$': ''},
            'R': {'a': '', '=': '', '+': 'lambda', '-': 'lambda', '/': '/FR', '*': '*FR', '(': '', ')': 'lambda', '$': 'lambda'},
            'F': {'a': 'a', '=': '', '+': '', '-': '', '/': '', '*': '', '(': '(E)', ')': '', '$': ''}
        }

    def parse(self, input_string):
        stack = ['$', 'S']  # Start with S in the stack
        input_string += '$'
        i = 0
        print("Stack:", ''.join(stack), "\t\tInput:", input_string[i:])
        while len(stack) > 0:
            if stack[-1] == input_string[i]:
                print("Stack:", ''.join(stack), "\t\tInput:", input_string[i:])
                stack.pop()
                i += 1
            else:
                top_stack = stack[-1]
                next_input = input_string[i]
                if top_stack in self.parsing_table and next_input in self.parsing_table[top_stack]:
                    if self.parsing_table[top_stack][next_input] == 'lambda':
                        stack.pop()
                    else:
                        next_production = self.parsing_table[top_stack][next_input]
                        stack.pop()
                        if next_production != '':
                            for symbol in next_production[::-1]:
                                if symbol != 'lambda':
                                    stack.append(symbol)
                else:
                    print("Rejected\n")
                    return
        print("Accepted\n")

parser = PredictiveParser()
parser.parse("a=(a+a)*a$")
parser.parse("a=a*(a-a)$")
parser.parse("a=(a+a)a$")
