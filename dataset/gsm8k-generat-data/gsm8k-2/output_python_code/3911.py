def solution():
    """Quincy just bought a car using a 5 year loan with no interest. He put $5,000.00 down as a down payment making his monthly payment $250.00. What is the price of the car?"""
    down_payment = 5000
    monthly_payment = 250
    total_payments = 5 * 12
    remaining_balance = total_payments * monthly_payment
    car_price = remaining_balance + down_payment
    result = car_price
    return result

print(solution())