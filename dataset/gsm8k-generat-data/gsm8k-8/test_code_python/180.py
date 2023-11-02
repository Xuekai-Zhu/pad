def solution():
    total_money = 960
    textbooks_cost = total_money / 2
    money_left = total_money - textbooks_cost
    school_supplies_cost = money_left / 4
    money_left -= school_supplies_cost
    result = money_left
    return result

print(solution())