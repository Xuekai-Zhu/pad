def solution():
    """Lee wants to propose marriage to Sierra. He wants to follow the adage that you should spend two months' salary on the ring. He earns $60,000 per year in salary and can save $1000 per month. How long will it take before he can propose to Sierra?"""
    annual_salary = 60000
    monthly_savings = 1000
    two_months_salary = annual_salary / 6
    months_to_save = two_months_salary / monthly_savings
    result = months_to_save
    return result

print(solution())