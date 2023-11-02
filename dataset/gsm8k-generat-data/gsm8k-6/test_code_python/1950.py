def solution():
    # Calculate the total cost of 5 chocolate bars
    chocolate_bars_cost = 5 * 2

    # Calculate the amount spent on 2 bags of chips
    spent_amount = 20 - 4 - chocolate_bars_cost

    # Calculate the cost of each bag of chips
    cost_per_bag = spent_amount / 2

    result = cost_per_bag
    return result

print(solution())