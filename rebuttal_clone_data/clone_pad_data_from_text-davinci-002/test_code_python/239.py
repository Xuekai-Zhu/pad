def solution():
    """Frank has 7 one-dollar bills, 4 five-dollar bills, 2 ten-dollar bills, and 1 twenty-dollar bill. He goes to buy peanuts, which cost $3 a pound. He buys what he wants and has $4 in change. He plans to eat the peanuts all in one week. How many pounds does he eat on average per day?"""
    money = 7 + (4 * 5) + (2 * 10) + (1 * 20)
    cost_per_pound = 3
    pounds_bought = (money - 4) / cost_per_pound
    days_in_a_week = 7
    average_daily_intake = pounds_bought / days_in_a_week
    result = average_daily_intake
    return result

print(solution())