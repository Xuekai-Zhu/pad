def solution():
    start_amount = 3000
    monthly_savings = 276
    savings_period = 48 # 4 years = 48 months
    secret_savings = 7000

    # Calculate the total savings from monthly contributions
    total_monthly_savings = monthly_savings * savings_period

    # Calculate the final amount with the secret savings added
    final_amount = start_amount + total_monthly_savings + secret_savings
    result = final_amount
    return result

print(solution())