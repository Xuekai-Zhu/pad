def solution():
    backpack_cost = 15
    pen_cost = 1
    pencil_cost = 1
    num_notebooks = 5
    total_spent = 32

    # Calculate the total cost of all notebooks
    total_notebooks_cost = total_spent - (backpack_cost + pen_cost + pencil_cost*2)

    # Calculate the cost per notebook
    cost_per_notebook = total_notebooks_cost / num_notebooks
    result = cost_per_notebook
    return result

print(solution())