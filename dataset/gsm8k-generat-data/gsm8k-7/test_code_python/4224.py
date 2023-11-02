def solution():
    num_green_notebooks = 2
    black_cost = 15
    pink_cost = 10
    total_cost = 45

    # Calculate the total cost of the green notebooks
    green_total_cost = total_cost - black_cost - pink_cost

    # Calculate the cost per green notebook
    green_cost_each = green_total_cost / num_green_notebooks

    result = green_cost_each
    return result

print(solution())