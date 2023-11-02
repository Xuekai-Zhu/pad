def solution():
    down_payment = 5000  # Quincy made a down payment of $5,000.00
    monthly_payment = 250  # Quincy's monthly payment is $250.00
    years = 5  # Quincy has a 5 year loan

    # Calculate the total amount paid over the life of the loan
    total_payments = monthly_payment * 12 * years
    total_payments += down_payment

    # Calculate the price of the car
    price_of_car = total_payments

    result = price_of_car
    return result

print(solution())