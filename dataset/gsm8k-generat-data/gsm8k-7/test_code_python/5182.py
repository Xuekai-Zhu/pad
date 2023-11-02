def solution():
    num_wands = 3
    profit_per_wand = 5
    total_profit = 2 * profit_per_wand # Kate only made profit on the wands sold to her friends

    # Calculate the total amount paid by Kate for all three wands
    total_cost = (130 - total_profit) / 3

    # Calculate the cost per wand
    cost_per_wand = total_cost / num_wands
    result = cost_per_wand
    return result

print(solution())