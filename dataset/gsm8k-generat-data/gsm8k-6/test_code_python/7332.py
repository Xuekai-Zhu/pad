def solution():
    # Calculate the cost of the first 3 pieces of art
    cost_first_three = 45000 / 3

    # Calculate the cost of the 4th piece of art
    cost_fourth = cost_first_three * 1.5

    # Calculate the total cost of all the art
    total_cost = cost_first_three * 3 + cost_fourth
    result = total_cost
    return result

print(solution())