def solution():
    """Brianne saves $10 in January. Each month, she saves twice as much as her previous month's savings. How much will she save in May?"""
    january_savings = 10
    february_savings = january_savings * 2
    march_savings = february_savings * 2
    april_savings = march_savings * 2
    may_savings = april_savings * 2
    result = may_savings
    return result

print(solution())