def solution():
    """Danielle bought a new house for $280k. She paid a $40k deposit on the house, and pays the rest using a mortgage that is spread out over 10 years. Danielle makes equal payments every month and at the end of the 10 years, the entire balance will be paid off. How much, in thousands of dollars, does Danielle pay each month?"""
    total_cost = 280000
    deposit = 40000
    balance = total_cost - deposit
    years = 10
    months = years * 12
    monthly_payment = balance / months / 1000
    result = monthly_payment
    return result

print(solution())