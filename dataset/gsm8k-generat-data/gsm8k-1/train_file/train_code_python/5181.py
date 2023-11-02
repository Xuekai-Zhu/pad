def solution():
    """While at Wizards Park, Kate buys 3 magic wands, one for herself and two for her friends. When she returns she sells the wands to her friends for $5 more than she paid. If she collected $130 after the sale, how much money did each wand cost?"""
    wands_bought = 3
    wands_sold = 2
    profit_per_wand = 5
    total_profit = 130
    cost_per_wand = (total_profit / wands_sold) - profit_per_wand
    result = cost_per_wand
    return result

print(solution())