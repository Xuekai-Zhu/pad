def solution():
    # Define the cost of each item
    banana_cost = 4
    pear_cost = 2
    asparagus_cost = 6
    chicken_cost = 11

    # Calculate the total cost of the items
    total_cost = 2 * banana_cost + pear_cost + asparagus_cost + chicken_cost

    # Calculate how much money Mom has left
    money_left = 55 - total_cost
    result = money_left
    return result

print(solution())