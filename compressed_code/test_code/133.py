def solution():
    
    total_money = 960
    textbook_cost = total_money / 2
    remaining_money = total_money - textbook_cost
    school_supplies_cost = remaining_money / 4
    money_left = total_money - textbook_cost - school_supplies_cost
    result = money_left
    return result

print(solution())