def solution():
    nuts = 3  # Adam bought 3 kilograms of nuts
    dried_fruits = 2.5  # Adam bought 2.5 kilograms of dried fruits
    cost_nuts_per_kg = 12  # The cost of one kilogram of nuts is $12
    cost_dried_fruits_per_kg = 8  # The cost of one kilogram of dried fruits is $8

    # Calculate the cost of the nuts and dried fruits
    cost_nuts = nuts * cost_nuts_per_kg
    cost_dried_fruits = dried_fruits * cost_dried_fruits_per_kg

    # Calculate the total cost
    total_cost = cost_nuts + cost_dried_fruits
    result = total_cost
    return result

print(solution())