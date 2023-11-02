def solution():
    
    hourly_wage_1 = 10
    hourly_wage_2 = 20
    hourly_wage_3 = 40
    hours_1 = 20
    hours_2 = 30
    hours_3 = 5
    expenses = 500
    earnings = (hourly_wage_1 * hours_1) + (hourly_wage_2 * hours_2) + (hourly_wage_3 * hours_3)
    net_earnings = earnings - expenses
    result = net_earnings
    return result

print(solution())