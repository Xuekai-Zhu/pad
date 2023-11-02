def solution():
    """Tommy's home is worth 25% more than he bought it for. He sells it and buys a new house that costs $500,000. If he had to take a loan for the 75% he can't pay, how much did he buy his first house for?"""
    # Define the cost of the new house and the percentage of the cost that Tommy can pay
    new_house_cost = 500000
    payment_percentage = 0.25

    # Calculate the amount of money Tommy can pay for the new house
    payment = new_house_cost * payment_percentage

    # Calculate the amount of money Tommy needs to borrow
    loan_amount = new_house_cost - payment

    # Calculate the original cost of Tommy's home
    original_cost = payment / 1.25

    # Return the result
    result = original_cost
    return result

print(solution())