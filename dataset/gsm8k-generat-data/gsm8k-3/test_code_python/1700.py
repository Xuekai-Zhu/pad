def solution():
    """Mike wants to buy a new car. He has chosen a red car for $35000. To be able to pay this price, he needs to loan part of the money from the bank, at a rate of 15%. How much money in total will Mike need to pay for the car, if he has to take $20000 from the bank?"""
    # Define the cost of the car and the loan interest rate
    CAR_COST = 35000
    INTEREST_RATE = 0.15

    # Define the amount of the loan
    loan_amount = 20000

    # Calculate the interest on the loan
    loan_interest = loan_amount * INTEREST_RATE

    # Calculate the total cost of the car, including the loan
    total_cost = CAR_COST + loan_interest

    # Display the total cost
    result = total_cost
    return result

print(solution())