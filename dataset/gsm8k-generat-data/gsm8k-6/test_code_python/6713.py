def solution():
    # Calculate the cost of making the blueberry pie
    cost_blueberry = (2 + 1 + 1.5) + (3 * 2.25 / 16)  # cost of ingredients + cost of blueberries
    # Calculate the cost of making the cherry pie
    cost_cherry = (2 + 1 + 1.5) + (14 / 4)  # cost of ingredients + cost of cherries
    # Compare the costs and return the cheaper one
    if cost_blueberry < cost_cherry:
        result = cost_blueberry
    else:
        result = cost_cherry
    return result

print(solution())