def solution():
    # Calculate the total cost of the items Jimmy bought
    pens_cost = 3 * 1  # Jimmy bought 3 pens for $1 each
    notebooks_cost = 4 * 3  # Jimmy bought 4 notebooks for $3 each
    folders_cost = 2 * 5  # Jimmy bought 2 folders for $5 each
    total_cost = pens_cost + notebooks_cost + folders_cost  # total cost of the items

    # Calculate the amount of change Jimmy will get back
    change = 50 - total_cost
    result = change
    return result

print(solution())