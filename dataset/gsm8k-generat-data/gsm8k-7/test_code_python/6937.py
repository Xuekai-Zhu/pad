def solution():
    sugar_price_per_kg = 1.5
    salt_price_per_kg = (5.5 - (2 * sugar_price_per_kg)) / 5
    # Solve for salt_price_per_kg using the given information

    num_sugar_kgs = 3
    num_salt_kgs = 1

    # Calculate the total cost of sugar
    total_sugar_cost = num_sugar_kgs * sugar_price_per_kg

    # Calculate the total cost of salt
    total_salt_cost = num_salt_kgs * salt_price_per_kg

    # Calculate the total cost of three kilograms of sugar and a kilogram of salt
    total_cost = total_sugar_cost + total_salt_cost
    result = total_cost
    return result

print(solution())