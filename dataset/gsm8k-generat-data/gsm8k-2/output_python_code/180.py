def solution():
    """Derek has $960 to buy his books for the semester. He spends half of that on his textbooks, and he spends a quarter of what is left on his school supplies. What is the amount of money Derek has left?"""
    total_money = 960
    textbook_cost = total_money / 2
    remaining_money = total_money - textbook_cost
    school_supplies_cost = remaining_money / 4
    money_left = total_money - textbook_cost - school_supplies_cost
    result = money_left
    return result

print(solution())