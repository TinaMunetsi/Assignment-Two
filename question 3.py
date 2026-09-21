# A list comprehension is a concise way of creating a new list
# from an existing sequence or range.
#
# It allows iteration, filtering and transformation to be
# performed in a single expression.
#
# The general syntax of a list comprehension is:
#
# [expression for item in iterable if condition]
#
# The expression determines what will be placed in the new
# list.
#
# The for statement specifies the items that will be processed.
#
# The if condition is optional and is used to filter the items.
#
# In this question, the number must satisfy two conditions:
#
# 1. The number must be odd.
# 2. The number must be divisible by 3.
#
# The range starts at 1 and stops before 51 so that numbers
# from 1 to 50 are considered.

odd_numbers_divisible_by_3 = [
    number
    for number in range(1, 51)
    if number % 2 != 0 and number % 3 == 0
]

print("Odd numbers between 1 and 50 divisible by 3:")
print(odd_numbers_divisible_by_3)
