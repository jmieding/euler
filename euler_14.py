# The following iterative sequence is defined for the set of positive integers:

# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 
# 10 terms. Although it has not been proved yet (Collatz Problem), it is thought 
# that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.


def get_longest_collatz_sequence(nums):
  longest_collatz_sequence = 0
  best_start_num = 0
  for num in nums:
    start_num = num
    collatz_length_current = 1
    while num > 1:
      if num % 2 == 0:
        num /= 2
      else:
        num = (num * 3) + 1
      collatz_length_current += 1
    if collatz_length_current > longest_collatz_sequence:
      longest_collatz_sequence, best_start_num = collatz_length_current, start_num
  return longest_collatz_sequence, best_start_num

test = xrange(1000000)

print get_longest_collatz_sequence(test)