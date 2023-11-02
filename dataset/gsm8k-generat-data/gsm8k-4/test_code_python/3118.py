def solution():
    """Jason is trying to figure out whether he can afford a new car. The car he wants costs $32,000, and he can make a down payment of $8,000. He'll have to get a loan for the rest of the amount and make 48 equal monthly payments on it. Each month, he also has to pay interest equal to 5% of that month's payment. How much will Jason's monthly payments be?"""
    # Define the cost of the car and the down payment
    CAR_COST = 32000
    DOWN_PAYMENT = 8000

    # Calculate the loan amount
    loan_amount = CAR_COST - DOWN_PAYMENT

    # Calculate the monthly payment amount before interest
    monthly_payment = loan_amount / 48

    # Calculate the total interest paid over the life of the loan
    total_interest = 0
    for i in range(1, 49):
        monthly_interest = monthly_payment * 0.05
        total_interest += monthly_interest

    # Calculate the total amount paid over the life of the loan
    total_cost = CAR_COST + total_interest - DOWN_PAYMENT

    # Calculate the monthly payment amount including interest
    monthly_payment_with_interest = total_cost / 48

    # Return the result
    result = monthly_payment_with_interest
    return result

print(solution())