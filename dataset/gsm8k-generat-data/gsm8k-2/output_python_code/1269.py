def solution():
    """Danielle bought a new house for $280k. She paid a $40k deposit on the house, and pays the rest using a mortgage that is spread out over 10 years. Danielle makes equal payments every month and at the end of the 10 years, the entire balance will be paid off. How much, in thousands of dollars, does Danielle pay each month?"""
    total_price = 280
    deposit = 40
    remaining_price = total_price - deposit
    num_months = 10 * 12
    monthly_payment = remaining_price / num_months
    result = monthly_payment / 1000
    return result

print(solution())