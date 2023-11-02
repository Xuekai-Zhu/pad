def solution():
    
    paycheck = 2400
    retirement_percent = 0.5
    car_percent = 0.2
    retirement_payment = paycheck * retirement_percent
    car_payment = paycheck * car_percent
    total_spent = retirement_payment + car_payment
    money_left = paycheck - total_spent
    result = money_left
    return result

print(solution())