def solution():
    """Greta's paycheck is $2400.00. She puts 50% of her pay into her retirement account. She then uses 20% of her paycheck to make her monthly car payment. After funding her retirement and paying for her car, how much money does she have left to spend?"""
    paycheck = 2400.00
    retirement_percent = 50
    car_payment_percent = 20
    retirement_amount = paycheck * (retirement_percent / 100)
    car_payment_amount = paycheck * (car_payment_percent / 100)
    remaining_money = paycheck - retirement_amount - car_payment_amount
    result = remaining_money
    return result

Note: For the Samantha's last name problem, a solution with programming code cannot be provided since the information provided is insufficient and confusing.

print(solution())