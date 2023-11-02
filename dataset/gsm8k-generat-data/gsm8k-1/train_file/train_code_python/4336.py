def solution():
    """Carrie worked for 2 hours a day for 4 days to make and decorate a wedding cake. She was paid $22 an hour. The cost for supplies to make the cake was $54. How much profit did Carrie earn on the cake?"""
    hours_per_day = 2
    days_worked = 4
    wage_per_hour = 22
    total_wage = hours_per_day * days_worked * wage_per_hour
    supply_cost = 54
    profit = total_wage - supply_cost
    result = profit
    return result

print(solution())