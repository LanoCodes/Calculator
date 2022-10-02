#Calculator
import os
from art import logo

def cls():
  os.system('cls' if os.name == 'nt' else 'clear')

#Addition
def add(n1, n2):
  return n1 + n2

#Subtraction
def subtract(n1, n2):
  return n1 - n2
  
#Mutliplication
def multiply(n1, n2):
  return n1 * n2
  
#Division
def divide(n1, n2):
  return n1 / n2


operations = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '/': divide
}

def calculator():
  print(logo)

  continue_calculating = 'y'
  
  num1 = float(input('What\'s your first number?: '))
  for sym in operations:
    print(sym)
    
  
  while continue_calculating == 'y':
    operation_symbol = input('\nPick an operation: ')
    num2 = float(input('What\'s your next number?: '))
  
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f'\n{num1} {operation_symbol} {num2} = {answer}\n')
    
    continue_calculating = input(f'\nType "y" to continue calculating with {answer}, or type "n" to exit.: ')
    if continue_calculating == 'y':
      num1 = answer
    else:
      cls()
      calculator()

calculator()