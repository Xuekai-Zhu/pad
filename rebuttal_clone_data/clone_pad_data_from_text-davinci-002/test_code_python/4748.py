def solution():
    money_left = 15
    money_spent_by_doris = 6
    money_spent_by_martha = money_spent_by_doris / 2
    total_money_spent = money_spent_by_doris + money_spent_by_martha
    initial_amount = money_left + total_money_spent
    result = initial_amount
    return result

print(solution())