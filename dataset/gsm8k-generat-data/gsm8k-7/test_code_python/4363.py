def solution():
    apple_weight = 5  # kilograms
    apple_price_per_kg = 2  # dollars

    sugar_packs = 3
    sugar_price = apple_price_per_kg - 1  # one pack of sugar is $1 cheaper than one kilogram of apples

    walnut_weight = 0.5  # kilograms
    walnut_price_per_kg = 6  # dollars

    # Calculate the total cost of apples
    apple_cost = apple_weight * apple_price_per_kg

    # Calculate the total cost of sugar
    sugar_cost = sugar_packs * sugar_price

    # Calculate the total cost of walnuts
    walnut_cost = walnut_weight * walnut_price_per_kg

    # Calculate the total cost of all items
    total_cost = apple_cost + sugar_cost + walnut_cost
    result = total_cost
    return result

print(solution())