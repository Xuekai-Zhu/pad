def solution():
    hours_worked = 8
    average_hourly_wage = 18
    total_money_made = hours_worked * average_hourly_wage
    money_spent = total_money_made / 2
    money_left = total_money_made - money_spent
    result = money_left
    return result

print(solution())