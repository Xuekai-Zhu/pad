def solution():
    """Frank has 7 one-dollar bills, 4 five-dollar bills, 2 ten-dollar bills, and 1 twenty-dollar bill. He goes to buy peanuts, which cost $3 a pound. He buys what he wants and has $4 in change. He plans to eat the peanuts all in one week. How many pounds does he eat on average per day?"""
    total_money = 7*1 + 4*5 + 2*10 + 1*20
    cost_per_pound = 3
    money_left = total_money - cost_per_pound - 4
    pounds_bought = money_left / cost_per_pound
    days_in_week = 7
    average_pounds_per_day = pounds_bought / days_in_week
    result = average_pounds_per_day
    return result

print(solution())