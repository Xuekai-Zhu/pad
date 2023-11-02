def solution():
    # Calculate the total cost of each item
    broccoli_cost = 4 * 3
    orange_cost = 0.75 * 3
    cabbage_cost = 3.75
    bacon_cost = 3
    chicken_cost = 3 * 2

    # Calculate the total cost of the groceries
    total_cost = broccoli_cost + orange_cost + cabbage_cost + bacon_cost + chicken_cost

    # Calculate the percentage of the budget spent on meat
    meat_cost = bacon_cost + chicken_cost
    meat_percentage = round((meat_cost / total_cost) * 100)

    result = meat_percentage
    return result

print(solution())