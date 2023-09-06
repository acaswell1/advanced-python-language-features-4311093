# Example file for Advanced Python: Language Features by Joe Marini
# Simple pattern matching using literal values

X = "Zero"

# Literal patterns are explicit values: integers, strings, Booleans, etc
match X:
    case 0:
        print("Zero")
    case "Zero":
        print(0)
    case 1:
        print("One")
    case None:
        print("Nothing")
    case _:
        print("no match")
