def solution():
    """Derek has $960 to buy his books for the semester. He spends half of that on his textbooks, and he spends a quarter of what is left on his school supplies. What is the amount of money Derek has left?"""
    initial_money = 960
    textbooks_cost = initial_money / 2
    money_left = initial_money - textbooks_cost
    school_supplies_cost = money_left / 4
    money_left = money_left - school_supplies_cost
    result = money_left
    
    return result

print(solution())