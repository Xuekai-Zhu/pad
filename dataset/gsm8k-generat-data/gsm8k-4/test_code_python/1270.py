def solution():
    """Danielle bought a new house for $280k. She paid a $40k deposit on the house, and pays the rest using a mortgage that is spread out over 10 years. Danielle makes equal payments every month and at the end of the 10 years, the entire balance will be paid off. How much, in thousands of dollars, does Danielle pay each month?"""
    # Define the total cost of the house and the deposit paid
    total_cost = 280000
    deposit = 40000

    # Calculate the remaining balance to be paid
    balance = total_cost - deposit

    # Calculate the number of months for the mortgage
    num_months = 10 * 12

    # Divide the balance by the number of months to get the monthly payment
    monthly_payment = balance / num_months / 1000

    result = monthly_payment
    return result

print(solution())