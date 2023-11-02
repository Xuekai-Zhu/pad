def solution():
    fix_cost = 20000
    discount = 20
    race_win = 70000
    percent_discount = fix_cost * (discount / 100)
    final_cost = fix_cost - percent_discount
    percent_race_money = 0.9
    race_money = race_win * percent_race_money
    money_made = race_money - final_cost
    result = money_made
    return result

print(solution())