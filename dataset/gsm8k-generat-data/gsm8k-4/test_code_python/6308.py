def solution():
    """Mr. Dubois buys a new car for $13,380. He pays $5,400 and pays the rest by giving $420 a month. In how many months will the car be fully paid for?"""
    # Define the initial cost of the car and the down payment
    CAR_COST = 13380
    DOWN_PAYMENT = 5400

    # Calculate the remaining balance
    balance = CAR_COST - DOWN_PAYMENT

    # Calculate the number of months needed to pay off the balance
    months = balance / 420

    result = round(months)
    return result

print(solution())