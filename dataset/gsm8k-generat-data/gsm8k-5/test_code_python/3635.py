def solution():
    total_notebooks = 12  # Mike bought a total of 12 notebooks
    red_notebooks = 3  # Mike bought 3 red notebooks
    green_notebooks = 2  # Mike bought 2 green notebooks
    blue_notebooks = total_notebooks - red_notebooks - green_notebooks  # Mike bought the rest as blue notebooks
    total_cost = 37  # Mike spent 37 dollars in total

    # Calculate the cost of the red notebooks
    red_cost = red_notebooks * 4

    # Calculate the cost of the green notebooks
    green_cost = green_notebooks * 2

    # Calculate the total cost of the blue notebooks
    blue_cost = total_cost - red_cost - green_cost

    # Calculate the cost of each blue notebook
    cost_per_blue_notebook = blue_cost / blue_notebooks
    result = cost_per_blue_notebook
    return result

print(solution())