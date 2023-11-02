def solution():
    """Mr. Dubois buys a new car for $13,380. He pays $5,400 and pays the rest by giving $420 a month. In how many months will the car be fully paid for?"""
    total_cost = 13380
    down_payment = 5400
    monthly_payment = 420
    remaining_balance = total_cost - down_payment
    months_to_pay = remaining_balance / monthly_payment
    result = months_to_pay
    return result

print(solution())