def solution():
    """Quincy just bought a car using a 5 year loan with no interest.  He put $5,000.00 down as a down payment making his monthly payment $250.00.  What is the price of the car?"""
    # Define the values given in the problem
    down_payment = 5000
    monthly_payment = 250
    loan_length_years = 5
    loan_length_months = loan_length_years * 12

    # Calculate the total amount paid over the life of the loan
    total_paid = down_payment + (monthly_payment * loan_length_months)

    # Calculate the price of the car
    car_price = total_paid

    # Display the price of the car
    result = car_price
    return result

print(solution())