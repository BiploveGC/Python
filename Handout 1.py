class Stack:
   def __init__(self):  # Corrected double underscore for constructor
       "Initialize an empty stack."
       self.items = []

   def is_empty(self):
       "Check if stack is empty"
       return len(self.items) == 0

   def push(self, item):
       "Push an item onto the stack. "
       self.items.append(item)

   def pop(self):
       "Pop an item from the stack."
       if not self.is_empty():
           return self.items.pop()
       else:
           raise IndexError("Pop from an empty stack")

   def peek(self):
       "Peek at the top item of the stack. "
       if not self.is_empty():
           return self.items[-1]
       else:
           raise IndexError("Peek from an empty stack")


def evaluate_postfix(expression, values):
   "Evaluate a postfix expression."""
   stack = Stack()
   for char in expression:
       if char.isalpha():
           # If the character is a variable, push its corresponding value
           stack.push(values[char])
       elif char in "+-*/":
           # If the character is an operator, perform the operation
           operand2 = stack.pop()
           operand1 = stack.pop()
           if char == '+':
               stack.push(operand1 + operand2)
           elif char == '-':
               stack.push(operand1 - operand2)
           elif char == '*':
               stack.push(operand1 * operand2)
           elif char == '/':
               stack.push(operand1 / operand2)
   # The final result should be on the top of the stack
   return stack.pop()

def main():
   values = {}  # Initialize values outside the loop
   while True:
       if not values:  # Prompt for values only if they're not yet set
           values_input = input("Enter the values of a, b, c, and d (separated by spaces): ")
           try:
               values = dict(zip("abcd", map(int, values_input.split())))
           except ValueError:
               print("Invalid input. Please enter four integers separated by spaces.")
               continue  # Skip to the next iteration if invalid input

       while True:  # Inner loop for evaluating multiple expressions with the same values
           postfix_expression = input("Enter a postfix expression with $ at the end: ")
           # Check for the end of input
           if postfix_expression.endswith("$"):
               result = evaluate_postfix(postfix_expression[:-1], values)
               print(f"Value = {result}")
               break  # Break out of the inner loop to prompt for continuation
           else:
               print("Invalid postfix expression. Please end with $.")

       continue_input = input("CONTINUE (y/n)? ").lower()
       if continue_input != 'y':
           break

if __name__ == "__main__":
   main()
