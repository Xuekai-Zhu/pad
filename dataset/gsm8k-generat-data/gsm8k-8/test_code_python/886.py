def solution():
    # Calculate the initial cost of water bottles
    initial_cost = 4 * 2

    # Calculate the cost of additional water bottles
    additional_cost = 2 * initial_cost

    # Calculate the cost of cheese
    cheese_cost = 0.5 * 10

    # Calculate the total cost of all items
    total_cost = initial_cost + additional_cost + cheese_cost

    # Calculate the remaining money
    remaining_money = 100 - total_cost
    result = remaining_money
    return result

print(solution())