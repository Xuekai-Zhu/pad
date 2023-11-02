def solution():
    # Calculate the total cost of the red and green notebooks
    red_notebook_cost = 3 * 4
    green_notebook_cost = 2 * 2
    total_cost = red_notebook_cost + green_notebook_cost

    # Calculate the cost of the blue notebooks
    blue_notebook_cost = 37 - total_cost

    # Calculate the cost of each blue notebook
    cost_per_blue_notebook = blue_notebook_cost / (12 - 3 - 2)
    result = cost_per_blue_notebook
    return result

print(solution())