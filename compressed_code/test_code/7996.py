def solution():
    
    monthly_income = 6000
    rent = 640
    food_expense = 380
    utilities = monthly_income / 4
    insurance = monthly_income / 5
    total_expense = rent + food_expense + utilities + insurance
    money_left = monthly_income - total_expense
    result = money_left
    return result

print(solution())