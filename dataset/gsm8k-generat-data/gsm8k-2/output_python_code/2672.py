def solution():
    """It took Alice three months to save up to buy new shoes. If she saved 10 dollars the first month and 30 more each month, how much did she have saved by the end of the third month?"""
    first_month_savings = 10
    monthly_increase = 30
    total_savings = first_month_savings + (monthly_increase * 2)
    result = total_savings
    return result

print(solution())