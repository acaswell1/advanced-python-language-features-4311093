# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for comprehensions

from string import punctuation as pct
import pprint


TEST_STR = "2 apples, 9 oranges?, 4 pears, Mike's 1 egg, Jane's 2 kiwis, $50!"

# YOUR CODE HERE
num_digits = len([digit for digit in TEST_STR if digit.isdigit()])
num_pct = len([punct for punct in TEST_STR if punct in pct])
NUM_CHARS = len(TEST_STR)
UNQ_LTTR_STR = ''.join({char for char in TEST_STR if char.isalpha()})

# print the data
str_data = {
    'Length': NUM_CHARS,
    'Digits': num_digits,
    'Punctuation': num_pct,
    'Unique Letters': UNQ_LTTR_STR,
    'Unique Count': len(UNQ_LTTR_STR)
}
pprint.pp(str_data)
