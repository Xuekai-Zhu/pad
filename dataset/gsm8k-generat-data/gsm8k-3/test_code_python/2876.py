def solution():
    """Aaron wants to purchase a guitar under a payment plan of $100.00 per month for 12 months.  His father has agreed to lend him the entire amount for the guitar, plus a one-time 10% interest fee for the entire loan.  With interest, how much money will Aaron owe his dad?"""
    # Define the loan amount and interest rate
    loan_amount = 1200
    interest_rate = 0.1

    # Calculate the interest amount
    interest_amount = loan_amount * interest_rate

    # Calculate the total amount to be repaid
    total_amount = loan_amount + interest_amount

    # Display the total amount
    result = total_amount
    return result

print(solution())