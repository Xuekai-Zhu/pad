def solution():
    """Frank has 7 one-dollar bills, 4 five-dollar bills, 2 ten-dollar bills, and 1 twenty-dollar bill. He goes to buy peanuts, which cost $3 a pound. He buys what he wants and has $4 in change. He plans to eat the peanuts all in one week. How many pounds does he eat on average per day?"""
    total_money = (7*1) + (4*5) + (2*10) + (1*20)
    peanuts_cost = 3
    total_spent = total_money - 4
    total_pounds = total_spent / peanuts_cost
    pounds_per_day = total_pounds / 7
    result = pounds_per_day
    return result

print(solution())