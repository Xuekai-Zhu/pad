def solution():
    # Calculate the total cost of pens
    pens_cost = 3 * 1  # Jimmy bought 3 pens for $1 each

    # Calculate the total cost of notebooks
    notebooks_cost = 4 * 3  # Jimmy bought 4 notebooks for $3 each

    # Calculate the total cost of folders
    folders_cost = 2 * 5  # Jimmy bought 2 folders for $5 each

    # Calculate the total cost of all items
    total_cost = pens_cost + notebooks_cost + folders_cost

    # Calculate the change from a $50 bill
    change = 50 - total_cost
    result = change
    return result

print(solution())