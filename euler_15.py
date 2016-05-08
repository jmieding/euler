"""
Starting in the top left corner of a 2 x 2 grid, and only being able to move to 
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20 x 20 grid?
"""

# This problem relies on a Combinations formula. To determine the total number
# comnbinations, the factorial of the total number of steps is divided by the
# product of the factorial of the number in a given subset (which, in our case,
# can be either the x axis or the y axis steps) and the factorial of 
# the difference of the total number and the subset.

# In other words: n!/r!(n - r)!

from math import factorial

def number_of_routes(steps_x, steps_y):
  total_steps = steps_x + steps_y
  total_steps_factorial = factorial(total_steps)
  x_factorial = factorial(steps_x)
  k_factorial = factorial(total_steps - steps_x)
  return total_steps_factorial/(x_factorial * k_factorial)

print number_of_routes(20, 20)
