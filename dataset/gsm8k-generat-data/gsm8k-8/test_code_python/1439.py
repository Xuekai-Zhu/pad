def solution():
    # Calculate the total cost of the pizzas
    total_cost = 4 * 10

    # Add the tip to the total cost
    total_cost += 5

    # Subtract the amount paid from the total cost to get the change
    change = 50 - total_cost
    result = change
    return result

print(solution())