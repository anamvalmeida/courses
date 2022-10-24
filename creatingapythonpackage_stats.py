"""
    Creating a Python Package

Author: Ana M. Almeida
Date: 24.10.2022

Guide: https://github.com/anamvalmeida/courses/blob/Applied-AI/Creating_a_Python_Package_v2.pdf
"""

def mean(numbers):
    """
    This function returns the mean of the given list of numbers
    """
    return sum(numbers)/len(numbers)


def median(numbers):
    """
    This function returns median of the given list of numbers
    """
    numbers.sort()
   
    if len(numbers) % 2 == 0:
        median1 = numbers[len(numbers) // 2]
        median2 = numbers[len(numbers) // 2 - 1]
        mymedian = (median1 + median2) / 2
    else:
        mymedian = numbers[len(numbers) // 2]
    return mymedian
