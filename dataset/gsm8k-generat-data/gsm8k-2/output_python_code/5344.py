def solution():
    """Lee wants to propose marriage to Sierra. He wants to follow the adage that you should spend two months' salary on the ring. He earns $60,000 per year in salary and can save $1000 per month. How long will it take before he can propose to Sierra?"""
    salary = 60000
    monthly_savings = 1000
    ring_cost = 2 * (salary/12)
    months_needed = ring_cost/monthly_savings
    result = months_needed
    return result

print(solution())