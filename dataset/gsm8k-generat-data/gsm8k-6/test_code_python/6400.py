def solution():
    # Calculate the total cost of the pens and pencils
    pens_pencils_cost = 1 + 1  # pack of pens and pencils cost $1.00 each

    # Calculate the total cost of the notebooks
    notebooks_cost = 32 - 15 - pens_pencils_cost  # total cost of backpack, pens/pencils subtracted from total cost

    # Calculate the cost of one notebook
    cost_per_notebook = notebooks_cost / 5  # 5 multi-subject notebooks purchased
    result = cost_per_notebook
    return result

print(solution())