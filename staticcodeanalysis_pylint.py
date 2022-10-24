"""
    Static Code Analysis

Author: Ana M. Almeida
Date: 24.10.2022

Guide: https://github.com/anamvalmeida/courses/blob/Applied-AI/StaticCodeAnalysis_v2.pdf
"""

# Sample1
def add(number1, number2):
    return number1 + number2

num1 = 4
num2 = 5
total = add(num1, num2)
print("The sum of {} and {} is {}".format(num1, num2, total))


"""
DELETE THIS PART (do not know why the error occurs tho)

Instructions:
1. Open the cmd
2. Change the directory to the file location, using 'cd \Users\...'
3. Run 'pylint name_of_file.py'

Pylint goes through every line of code and gives you a list all the non-compliant lines.
Pylint gives you a compliance score (10 being maximum).


# Sample2
def add(number1, number2):
    return number1 + number2

NUM1 = 4
num2 = 5
total = add(NUM1, num2)
print("The sum of {} and {} is {}".format(NUM1, num2, total))
"""
