def solution():
    """Quincy just bought a car using a 5 year loan with no interest. He put $5,000.00 down as a down payment making his monthly payment $250.00. What is the price of the car?"""
    down_payment = 5000
    monthly_payment = 250
    months = 5 * 12
    total_paid = down_payment + (monthly_payment * months)
    price_of_car = total_paid
    return price_of_car

print(solution())