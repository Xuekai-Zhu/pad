def solution():
    monthly_income = 6000
    house_rent = 640
    food_expense = 380
    monthly_bill = monthly_income / 4
    insurance = monthly_income / 5
    money_left = monthly_income - house_rent - food_expense - monthly_bill - insurance
    result = money_left
    
    return result

print(solution())