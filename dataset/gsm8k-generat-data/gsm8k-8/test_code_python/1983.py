def solution():
    # Calculate the cost of the broccoli
    broccoli_cost = 3 * 4

    # Calculate the cost of the oranges
    oranges_cost = 3 * 0.75

    # Calculate the total cost of the meat
    meat_cost = 3 + (2 * 3)

    # Calculate the total cost of the grocery purchase
    total_cost = broccoli_cost + oranges_cost + 3.75 + meat_cost

    # Calculate the percentage spent on meat
    meat_percentage = round((meat_cost / total_cost) * 100)

    result = meat_percentage
    return result

print(solution())