"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

def sum_of_digits(num):
  nums = [int(digit) for digit in str(num)]
  total = sum(nums)
  return total

print sum_of_digits(2**1000)
