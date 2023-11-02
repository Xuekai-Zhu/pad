def solution():
    """Mary earns $20 washing cars and $40 walking dogs each month. If she puts half of that money away each month how long would it take her to save $150?"""
    monthly_income = 20 + 40
    monthly_savings = 0.5 * monthly_income
    target_savings = 150
    months_needed = target_savings / monthly_savings
    result = months_needed
    return result

print(solution())