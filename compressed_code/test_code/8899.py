def solution():
    
    hourly_rate = 30
    hours_per_week = 48
    weekly_pay = hourly_rate * hours_per_week
    monthly_income = weekly_pay * 4

    rent_portion = monthly_income / 3
    food_expense = 500
    tax_expense = 1000
    total_expenses = rent_portion + food_expense + tax_expense

    total_money_after_expenses = monthly_income - total_expenses
    result = total_money_after_expenses

    return result

print(solution())