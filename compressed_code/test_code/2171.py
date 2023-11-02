def solution():
    
    monthly_income = 6000
    rental_expense = 640
    food_expense = 380
    electric_water_expense = monthly_income * 0.25
    insurance_expense = monthly_income * 0.2
    total_expenses = rental_expense + food_expense + electric_water_expense + insurance_expense
    remaining_income = monthly_income - total_expenses
    result = remaining_income
    return result

print(solution())