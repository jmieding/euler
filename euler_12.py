"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

# The number of divisors of given number is equal to the exponents + 1 of the prime factors of the number.
# For example: 6 has 4 divisors (1, 2, 3, & 6). It's prime factors are 2 and 3, which can be written
# as 2^1 and 3^1. If we add 1 to each exponent we get 2^2 and 3^2. If we add the exponents, we get 4.
# For 8: it has 4 divisors (1, 2, 4, 8). It's prime is 2^3. Add one to get 4.

# So, for each number, you need to generate all prime factors, count the number of times each occurs,
# then add one to the exponents, and multiply them for the total number of factors.

def count_divisors(triangle_num):
  divisors = 1
  exponent = 0
  while triangle_num % 2 == 0:
    exponent += 1
    triangle_num /= 2
  divisors *= exponent + 1
  prime = 3
  while triangle_num > 1:
    exponent = 0
    while triangle_num % prime == 0:
      exponent += 1
      triangle_num /= prime
    prime += 2
    divisors *= exponent + 1
  return divisors

def generate_triangles():
  increment = 1
  triangle_num = 1
  while True:
    increment += 1
    triangle_num += increment
    total_divisors = count_divisors(triangle_num)
    if total_divisors > 500:
      return triangle_num, total_divisors
    else:
      print "num is {}. {} divisors is less than 500" .format(triangle_num, total_divisors)

print generate_triangles()