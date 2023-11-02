def solution():
    
    hourly_wage = 30
    weekly_hours = 48
    monthly_wage = hourly_wage * weekly_hours * 4
    rent = monthly_wage / 3
    food = 500
    taxes = 1000
    total_expenses = rent + food + taxes
    remaining_money = monthly_wage - total_expenses
    result = remaining_money
    return result

print(solution())