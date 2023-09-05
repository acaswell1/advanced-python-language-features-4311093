# Example file for Advanced Python: Language Features by Joe Marini
# Challenge solution file for Advanced Functions

# Challenge:
# Write a function that performs the following actions:
# 1: accepts a variable number of strings and numbers. Other types ignored
# 2: accepts a keyword-only argument to return a unique-only result
# 3: combines all the arguments into a single string
# 4: returns a string containing all arguments combined as one string
# 5: Has a docstring that explains how it works
# If the unique-only argument is True (default False), then the result
# combined string will not contain any duplicate characters


def string_combiner(*args, unique=False):
    """
    string_combiner(*args, unique=False) -> given strings or numbers,
    the string combiner method with combine them into a single string. 
    If set to true the unique field will require all chars in the sting
    to be totally unique. (NOTE: Types other than strings and ints ignored)

    Parameters:
    *args -> list of strings to combine
    unique -> boolean determining char uniqueness

    Returns:
    string made up of the strings passed to args
    """
    result = ""

    for entry in args:
        if isinstance(entry, (str, int)):
            entry = str(entry)
            for char in entry:
                if not unique or (unique and (result.find(char)) == -1):
                    result += char
    return result


# test code:
print(string_combiner.__doc__)
output = string_combiner("This", "is", 1, "test", "string!", unique=False)
print(output)
output = string_combiner("This", "is", 1, "test", "string!", unique=True)
print(output)
output = string_combiner("This", "is", 1, True, "string!", unique=False)
print(output)
output = string_combiner("This", "is", [1, 2], "string!", unique=False)
print(output)
