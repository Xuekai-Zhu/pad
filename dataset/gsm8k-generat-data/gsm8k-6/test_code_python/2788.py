def solution():
    monthly_income = 6000
    rental_expense = 640
    food_expense = 380
    utility_expense = monthly_income * (1/4)
    insurance_expense = monthly_income * (1/5)
    total_expenses = rental_expense + food_expense + utility_expense + insurance_expense
    money_left = monthly_income - total_expenses
    result = money_left
    return result

print(solution())