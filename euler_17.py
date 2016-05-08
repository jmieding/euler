"""
Euler Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out 
in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 
letters. The use of "and" when writing out numbers is in compliance with 
British usage.
"""

def length_of_numbers_spelled_out(num):
  import inflect
  p = inflect.engine()
  # you can learn more about Pypi's inflect package here: 
  # https://pypi.python.org/pypi/inflect
  
  numbers_as_words = ''

  for num in xrange(1, num + 1):
    numbers_as_words += p.number_to_words(num)

  remove_dashes = numbers_as_words.replace('-', '')
  remove_spaces = remove_dashes.replace(' ', '')
  return len(remove_spaces)

print length_of_numbers_spelled_out(1000)