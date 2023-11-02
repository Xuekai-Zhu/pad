def solution():
    wands_bought = 3
    wands_sold = 2
    money_collected = 130
    money_spent = money_collected - (wands_sold * 5)
    cost_per_wand = money_spent / wands_bought
    result = cost_per_wand
    
    return result

print(solution())