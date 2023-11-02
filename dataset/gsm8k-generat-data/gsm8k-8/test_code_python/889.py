def solution():
    iphone_cost = 800
    trade_in_value = 240
    weekly_income = 80

    remaining_cost = iphone_cost - trade_in_value
    weeks_needed = remaining_cost / weekly_income

    result = weeks_needed
    return result

print(solution())