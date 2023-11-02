def solution():
    
    monthly_income = 3200
    monthly_bills = 1250 + 150 + 400 + 300 + 200 + 200
    car_payment = 350
    remaining_money = monthly_income - monthly_bills - car_payment
    result = remaining_money
    return result

print(solution())