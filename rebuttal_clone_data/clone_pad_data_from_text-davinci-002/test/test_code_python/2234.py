def solution():
    hour_wage = 30
    hours_worked = 48
    weekly_pay = hour_wage * hours_worked
    monthly_pay = weekly_pay * 4
    rent = monthly_pay / 3
    food = 500
    taxes = 1000
    monthly_expenses = rent + food + taxes
    net_income = monthly_pay - monthly_expenses
    result = net_income
    return result

print(solution())