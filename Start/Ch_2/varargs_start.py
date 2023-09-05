# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate the use of lambda functions


# TODO: define a function that takes variable arguments
def addition(*args):
    res = 0
    for arg in args:
        res += arg
    return res


# TODO: pass different arguments
print(addition(5, 10, 15, 20))
print(addition(5, 15, 20))
print(addition(5, 20, 15, 20, -13))


# TODO: pass an existing list
my_nums = [5, 10, 15, 20, 25]
print(addition(*my_nums))