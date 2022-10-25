"""
    Creating a Python Package Testing

Author: Ana M. Almeida
Date: 24.10.2022

Guide: https://github.com/anamvalmeida/courses/blob/Applied-AI/UnitTesting_v2.pdf
"""

from python_package import first, second
first.python_first()
second.python_second()

from creatingapythonpackage import creatingapythonpackage_basic, creatingapythonpackage_stats
print(creatingapythonpackage_basic.square(2))
print(creatingapythonpackage_stats.mean([3,4,5]))
