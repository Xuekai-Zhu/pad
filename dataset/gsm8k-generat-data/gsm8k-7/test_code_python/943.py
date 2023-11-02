def solution():
    goal = 96
    cost_per_dozen = 2.4
    price_per_donut = 1

    # Calculate the total profit per dozen of donuts
    profit_per_dozen = (12 * price_per_donut) - cost_per_dozen

    # Calculate the number of dozens of donuts needed to reach the goal
    num_dozen = goal / profit_per_dozen

    result = num_dozen
    return result

print(solution())