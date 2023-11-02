def solution():
    """Quincy just bought a car using a 5 year loan with no interest. He put $5,000.00 down as a down payment making his monthly payment $250.00. What is the price of the car?"""
    # Calculate the total number of months in 5 years
    total_months = 5 * 12

    # Calculate the total amount paid in monthly payments
    total_payments = total_months * 250

    # Subtract the down payment from the total amount paid to get the price of the car
    car_price = total_payments + 5000

    # return the result
    result = car_price
    return result

print(solution())