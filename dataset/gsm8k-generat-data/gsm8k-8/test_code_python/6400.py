def solution():
    # Calculate the total spent on pens and pencils
    pens_and_pencil_cost = 2 * 1.00

    # Calculate the total spent on notebooks
    notebook_cost = 32 - 15 - pens_and_pencil_cost

    # Calculate the cost of one notebook
    cost_per_notebook = notebook_cost / 5
    result = cost_per_notebook
    return result

print(solution())