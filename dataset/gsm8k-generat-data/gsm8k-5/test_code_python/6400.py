def solution():
    # Calculate the total cost of everything except the notebooks
    total_cost_without_notebooks = 32 - 15 - 2  # $15 for the backpack, $1 for each pack of pens and pencils

    # Calculate the cost per notebook
    cost_per_notebook = total_cost_without_notebooks / 5

    result = cost_per_notebook
    return result

print(solution())