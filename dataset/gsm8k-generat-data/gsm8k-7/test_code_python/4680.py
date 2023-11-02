def solution():
    nuts_kg = 3
    nuts_price = 12

    fruits_kg = 2.5
    fruits_price = 8

    # Calculate the total cost of nuts
    total_nuts_cost = nuts_kg * nuts_price

    # Calculate the total cost of dried fruits
    total_fruits_cost = fruits_kg * fruits_price

    # Calculate the total cost of all purchases
    total_cost = total_nuts_cost + total_fruits_cost
    result = total_cost
    return result

print(solution())