def solution():
    """Danielle bought a new house for $280k. She paid a $40k deposit on the house, and pays the rest using a mortgage that is spread out over 10 years. Danielle makes equal payments every month and at the end of the 10 years, the entire balance will be paid off. How much, in thousands of dollars, does Danielle pay each month?"""
    # Calculate the total balance to be paid off
    balance = 280000 - 40000

    # Calculate the total number of months for the mortgage
    num_months = 10 * 12

    # Calculate the monthly payment needed to pay off the balance in 10 years
    monthly_payment = balance / num_months / 1000

    # Display the monthly payment
    result = monthly_payment
    return result

print(solution())