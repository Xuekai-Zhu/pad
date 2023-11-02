def solution():
    
    money = 7 + (4 * 5) + (2 * 10) + (1 * 20)
    cost_per_pound = 3
    pounds_bought = (money - 4) / cost_per_pound
    days_in_a_week = 7
    average_daily_intake = pounds_bought / days_in_a_week
    result = average_daily_intake
    return result

print(solution())