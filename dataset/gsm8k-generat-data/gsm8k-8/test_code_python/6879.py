def solution():
    # Calculate the total cost of the 28 toys
    toys_cost = 28 * 10

    # Calculate the total cost of all the toys
    total_cost = toys_cost + (20 * teddy_bear_cost)

    # Calculate the cost per teddy bear
    teddy_bear_cost = (580 - toys_cost) / 20

    return teddy_bear_cost

print(solution())