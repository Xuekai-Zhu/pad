def solution():
    """Dawn earns 48,000 a year in 12 equal monthly payments. Each month, she saves 10% of her salary. How much does she save each month?"""
    # Define Dawn's annual salary and monthly savings rate
    annual_salary = 48000
    savings_rate = 0.1

    # Calculate Dawn's monthly salary and monthly savings amount
    monthly_salary = annual_salary / 12
    monthly_savings = monthly_salary * savings_rate

    # Round the monthly savings amount to 2 decimal places
    result = round(monthly_savings, 2)
    return result

print(solution())