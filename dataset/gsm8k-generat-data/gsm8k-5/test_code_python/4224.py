def solution():
    # Calculate the total cost of the green notebooks and subtract it from the total cost
    total_cost = 45
    black_cost = 15
    pink_cost = 10
    green_total_cost = total_cost - black_cost - pink_cost

    # Calculate the cost of each green notebook
    green_notebook_cost = green_total_cost / 2
    result = green_notebook_cost
    return result

print(solution())