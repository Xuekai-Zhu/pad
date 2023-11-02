def solution():
    initial_savings = 3000  # Initial savings when Sheila bought the piggy bank
    monthly_savings = 276  # Amount Sheila continues to save per month
    savings_period = 4 * 12  # 4 years of monthly savings
    total_savings = initial_savings + (monthly_savings * savings_period)  # Total savings after 4 years of savings

    # Add the additional $7,000 from Sheila's family
    total_savings += 7000

    result = total_savings
    return result

print(solution())