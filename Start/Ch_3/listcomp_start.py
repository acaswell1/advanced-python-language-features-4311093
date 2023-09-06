# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate how to use list comprehensions


# define two lists of numbers
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# TODO: Perform a mapping and filter function on a list
print(list(filter(lambda x: x < 10, map(lambda x: x + 1, evens))))

# TODO: Derive a new list of numbers frm a given list
squared_odds = [odd ** 2 for odd in odds]
print(squared_odds)

# TODO: Limit the items operated on with a predicate condition
double_small_odds = [(odd * 2) for odd in odds if odd < 10]
print(double_small_odds)
