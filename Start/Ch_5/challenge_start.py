# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for Structural Pattern Matching

# Dry Clean: [garment, size, starch, same_day]
#   garments are shirt, pants, jacket, dress
#   each item is 12.95, plus 2.00 for starch
#   same day service adds 10.00 per same-day item
# Wash and Fold: [description, weight]
#   4.95 per pound, with 10% off if more than 15 pounds
# Blankets: [type, dryclean, size]
#   type is "comforter" or "cover"
#   Flat fee of 25.00
# ---
# Output:
# Order Total Price

test_orders = [
    [
        ["shirt", "L", True, False],
        ["shirt", "M", True, False],
        ["shirt", "L", False, True],
        ["pants", "M", False, True],
        ["pants", "S", False, False],
        ["pants", "S", False, False],
        ["jacket", "M", False, False],
        ["jacket", "L", False, True]
    ],
    [
        ["dress", "M", False, True],
        ["whites", 5.25],
        ["darks", 12.5]
    ],
    [
        ["shirts and jeans", 28.0],
        ["comforter", False, "L"],
        ["cover", True, "L"],
        ["shirt", "L", True, True]
    ]
]

# process each order

for order in test_orders:
    ORD_TOTAL = 0
    print("-----------------")
    for item in order:
        match item:
            case ["shirt" | "pants" | "jacket" | "dress", str(), bool(), bool()] \
                    as dry_cleaning:
                print(
                    f"Dry Cleaning:({dry_cleaning[1]}) {dry_cleaning[0]} ", end='')
                if dry_cleaning[2]:
                    print("Starched ", end='')
                    ORD_TOTAL += 2.00
                if dry_cleaning[3]:
                    print("same-day ", end='')
                    ORD_TOTAL += 10.00
                print()
                ORD_TOTAL += 12.95
            case [str(), float()] as wash_n_fold:
                description, weight = wash_n_fold[0], wash_n_fold[1]
                print(
                    f"Wash/Fold: {description}, weight: {weight:.1f}")
                item_price = weight * 4.95
                if weight > 15.00:
                    item_price *= 0.90
                ORD_TOTAL += item_price
            case ["comforter" | "cover", bool(), str()] as blankets:
                blnkt_type, dryclean, size = blankets[0], blankets[1], blankets[2]
                print(f"Blanket: ({size}) {blnkt_type}", end=" ")
                if dryclean:
                    print("Dry clean", end="")
                print()
                ORD_TOTAL += 25.00
            case _:
                print("Not found")
    print(f"Order Total: {ORD_TOTAL:.2f}")
    print("-----------------")
