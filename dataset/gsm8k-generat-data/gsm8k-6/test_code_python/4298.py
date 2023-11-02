def solution():
    # Calculate the cost of potatoes, tomatoes, cucumbers, and bananas
    potatoes_cost = 6 * 2
    tomatoes_cost = 9 * 3
    cucumbers_cost = 5 * 4
    bananas_cost = 3 * 5

    # Calculate the total cost of the groceries
    total_cost = potatoes_cost + tomatoes_cost + cucumbers_cost + bananas_cost

    # Calculate the remaining money
    remaining_money = 500 - total_cost
    result = remaining_money
    return result

print(solution())