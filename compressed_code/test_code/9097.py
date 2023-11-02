def solution():
    
    monthly_income = 3200
    monthly_expenses = 1250 + 150 + 400 + 300 + 200 + 200
    car_payment = 350
    remaining_income = monthly_income - monthly_expenses - car_payment
    result = remaining_income
    return result

print(solution())