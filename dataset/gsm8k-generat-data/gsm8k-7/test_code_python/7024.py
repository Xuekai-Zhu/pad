def solution():
    rice_weight = 5  # kilograms
    rice_price = 2  # dollars per kilogram
    meat_weight = 3  # pounds
    meat_price = 5  # dollars per pound

    # Convert meat weight to kilograms
    meat_weight_kg = meat_weight * 0.453592

    # Calculate the total cost of rice
    rice_cost = rice_weight * rice_price

    # Calculate the total cost of meat
    meat_cost = meat_weight_kg * meat_price

    # Calculate the total cost of both items
    total_cost = rice_cost + meat_cost
    result = total_cost
    return result

print(solution())