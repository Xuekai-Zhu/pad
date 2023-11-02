def solution():
    # Define the total cost and cost of black and pink notebooks
    total_cost = 45
    black_cost = 15
    pink_cost = 10

    # Calculate the cost of the two green notebooks
    green_cost = total_cost - black_cost - pink_cost

    # Calculate the cost of one green notebook
    one_green_cost = green_cost / 2
    result = one_green_cost
    return result

print(solution())