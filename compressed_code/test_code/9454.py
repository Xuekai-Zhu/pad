def solution():
    
    bike_cost = 100
    current_savings = 65
    weekly_allowance = 5
    lawn_payment = 10
    babysitting_hours = 2
    babysitting_rate = 7

    total_weekly_income = weekly_allowance + lawn_payment + (babysitting_hours * babysitting_rate)
    money_needed = bike_cost - current_savings - total_weekly_income
    result = money_needed
    return result

print(solution())