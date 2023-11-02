def solution():
    """Dawn earns 48,000 a year in 12 equal monthly payments. Each month, she saves 10% of her salary. How much does she save each month?"""
    annual_salary = 48000
    monthly_salary = annual_salary / 12
    savings_percent = 0.1
    monthly_savings = monthly_salary * savings_percent
    result = monthly_savings
    return result

print(solution())