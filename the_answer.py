"""
#######################################################
WARNING:

The code below contains the solution to the problem. 

ONLY refer to it after you've genuinely tried to 
solve the problem on your own. Struggling with a problem 
and trying to devise a solution on your own, even if not 
successful, is an essential part of the learning process.

Please ensure you've given it a fair attempt before diving 
into the solution.

#######################################################
"""


















































def add(num1, num2):
    try:
        result = float(num1) + float(num2)
        return result
    except ValueError:
        raise ValueError("Invalid input. Please provide valid numbers.")

def subtract(num1, num2):
    try:
        result = float(num1) - float(num2)
        return result
    except ValueError:
        raise ValueError("Invalid input. Please provide valid numbers.")

def multiply(num1, num2):
    try:
        result = float(num1) * float(num2)
        return result
    except ValueError:
        raise ValueError("Invalid input. Please provide valid numbers.")

def divide(num1, num2):
    try:
        result = float(num1) / float(num2)
        return result
    except ValueError:
        raise ValueError("Invalid input. Please provide valid numbers.")
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero.")

