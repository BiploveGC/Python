def parse(string, table):
  """
  Parses a string using the LR parsing table.

  Args:
    string: The input string to parse.
    table: The LR parsing table.

  Returns:
    True if the string is accepted, False otherwise.
  """
  stack = [0]  # Start with state 0 on the stack
  input_string = list(string) + ["$"]  # Add dollar sign to the end of the input string
  i = 0

  while True:
    state = stack[-1]
    symbol = input_string[i]

    if symbol in table[state]:
      action = table[state][symbol]
      if action[0] == "S":  # Shift
        stack.append(symbol)
        stack.append(int(action[1:]))
        i += 1
      elif action[0] == "R":  # Reduce
        rule_number = int(action[1:])
        # Get the right-hand side of the production rule
        rhs = productions[rule_number - 1].split()[2:]
        # Check if the RHS has at least 3 elements before slicing
        if len(rhs) >= 3:
            rhs = rhs[2:]
        # Pop the symbols from the stack corresponding to the RHS
        for _ in range(len(rhs)):
          stack.pop()
        # Get the left-hand side of the production rule
        lhs = productions[rule_number - 1].split()[0]
        # Look up the goto state for the new symbol on the stack
        stack.append(lhs)
        stack.append(table[stack[-2]][lhs])
      elif action == "ACC":  # Accept
        return True
    else:
      return False  # Error

# Productions for the grammar
productions = [
    "E -> E + T",
    "E -> T",
    "T -> T * F",
    "T -> F",
    "F -> ( E )",
    "F -> id",
    "E' -> E",
]

# LR parsing table (replace with your actual table from the image)
table = {
    0: {'i': 'S5', '+': '', '-': '', '*': '', '/': '', '(': 'S4', ')': '', '$': '', 'E': '1', 'T': '2', 'F': '3'},
    1: {'i': '', '+': 'S6', '-': 'S7', '*': '', '/': '', '(': '', ')': '', '$': 'ACC', 'E': '', 'T': '', 'F': ''},
    2: {'i': '', '+': 'R3', '-': 'R3', '*': 'S8', '/': 'S9', '(': '', ')': 'R3', '$': 'R3', 'E': '', '': '', 'F': ''},
    3: {'i': '', '+': 'R6', '-': 'R6', '*': 'R6', '/': 'R6', '(': '', ')': 'R6', '$': 'R6', 'E': '', 'T': '', 'F': ''},
    4: {'i': 'S5', '+': '', '-': '', '*': '', '/': '', '(': 'S4', ')': '', '$': '', 'E': '10', 'T': '2', 'F': '3'},
    5: {'i': '', '+': 'R8', '-': 'R8', '*': 'R8', '/': 'R8', '(': '', ')': 'R8', '$': 'R8', 'E': '', 'T': '', 'F': ''},
    6: {'i': 'S5', '+': '', '-': '', '*': '', '/': '', '(': 'S4', ')': '', '$': '', 'E': '', 'T': '11', 'F': '3'},
    7: {'i': 'S5', '+': '', '-': '', '*': '', '/': '', '(': 'S4', ')': '', '$': '', 'E': '', 'T': '12', 'F': '3'},
    8: {'i': 'S5', '+': '', '-': '', '*': '', '/': '', '(': 'S4', ')': '', '$': '', 'E': '', 'T': '', 'F': '13'},
    9: {'i': 'S5', '+': '', '-': '', '*': '', '/': '', '(': 'S4', ')': '', '$': '', 'E': '', 'T': '', 'F': '14'},
    10: {'i': '', '+': 'S6', '-': 'S7', '*': '', '/': '', '(': '', ')': 'S15', '$': '', 'E': '', 'T': '', 'F': ''},
    11: {'i': '', '+': 'R1', '-': 'R1', '*': 'S8', '/': 'S9', '(': '', ')': 'R1', '$': 'R1', 'E': '', 'T': '', 'F': ''},
    12: {'i': '', '+': 'R2', '-': 'R2', '*': 'S8', '/': 'S9', '(': '', ')': 'R2', '$': 'R2', 'E': '', 'T': '', 'F': ''},
    13: {'i': '', '+': 'R4', '-': 'R4', '*': 'R4', '/': 'R4', '(': '', ')': 'R4', '$': 'R4', 'E': '', 'T': '', 'F': ''},
    14: {'i': '', '+': 'R5', '-': 'R5', '*': 'R5', '/': 'R5', '(': '', ')': 'R5', '$': 'R5', 'E': '', 'T': '', 'F': ''},
    15: {'i': '', '+': 'R7', '-': 'R7', '*': 'R7', '/': 'R7', '(': '', ')': 'R7', '$': 'R7', 'E': '', 'T': '', 'F': ''}
}

# Test the input strings
string1 = "(i+i)*i$"
string2 = "(i*)$"

if parse(string1, table):
    print(f"String '{string1}' is accepted")
else:
    print(f"String '{string1}' is rejected")

if parse(string2, table):
    print(f"String '{string2}' is accepted")
else:
    print(f"String '{string2}' is rejected")
