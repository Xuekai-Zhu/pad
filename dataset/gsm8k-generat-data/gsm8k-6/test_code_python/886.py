def solution():
    # Calculate the total cost of 4 bottles of water
    cost_bottles_of_water = 4 * 2  # Each bottle cost $2

    # Calculate the total cost of the additional bottles of water
    additional_bottles_of_water = 4 * 2  # Jack bought twice as many bottles as he already bought
    cost_additional_bottles_of_water = additional_bottles_of_water * 2  # Each bottle costs $2

    # Calculate the total cost of the cheese
    cost_cheese = 10 / 2  # Jack bought half a pound of cheese and 1 pound of cheese costs $10

    # Calculate the total cost of the items Jack bought
    total_cost = cost_bottles_of_water + cost_additional_bottles_of_water + cost_cheese

    # Calculate the remaining money Jack has
    remaining_money = 100 - total_cost

    result = remaining_money
    return result

print(solution())