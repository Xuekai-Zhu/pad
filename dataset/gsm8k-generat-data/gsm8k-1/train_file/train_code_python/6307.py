def solution():
    """Mr. Dubois buys a new car for $13,380. He pays $5,400 and pays the rest by giving $420 a month. In how many months will the car be fully paid for?"""
    car_cost = 13380
    paid_off = 5400
    monthly_payment = 420
    amount_left = car_cost - paid_off
    months_to_pay = amount_left / monthly_payment
    result = months_to_pay
    return result

print(solution())