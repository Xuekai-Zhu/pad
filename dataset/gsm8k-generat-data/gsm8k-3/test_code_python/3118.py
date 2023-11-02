def solution():
    """Jason is trying to figure out whether he can afford a new car. The car he wants costs $32,000, and he can make a down payment of $8,000. He'll have to get a loan for the rest of the amount and make 48 equal monthly payments on it. Each month, he also has to pay interest equal to 5% of that month's payment. How much will Jason's monthly payments be?"""
    # Define the cost of the car and the down payment
    CAR_COST = 32000
    DOWN_PAYMENT = 8000

    # Calculate the amount of the loan
    loan_amount = CAR_COST - DOWN_PAYMENT

    # Define the number of monthly payments and the interest rate
    NUM_MONTHS = 48
    INTEREST_RATE = 0.05

    # Calculate the monthly payment
    monthly_interest_rate = INTEREST_RATE / 12
    numerator = monthly_interest_rate * loan_amount
    denominator = 1 - (1 + monthly_interest_rate)**(-NUM_MONTHS)
    monthly_payment = numerator / denominator

    # Display the monthly payment
    result = monthly_payment
    return result

print(solution())