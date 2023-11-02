def solution():
    """While at Wizards Park, Kate buys 3 magic wands, one for herself and two for her friends. When she returns she sells the wands to her friends for $5 more than she paid. If she collected $130 after the sale, how much money did each wand cost?"""
    num_wands = 3
    profit_per_wand = 5
    total_profit = 130
    total_cost = (total_profit / num_wands) - profit_per_wand
    cost_per_wand = total_cost / num_wands
    result = cost_per_wand
    return result

print(solution())