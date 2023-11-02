def solution():
    """Robert, a sales agent, earns a basic salary of $1250 per month and, 10% commission on his monthly sales. Last month, his total sales were $23600. He allocated 20% of his total earnings to savings and the rest of the money to his monthly expenses. How much were his monthly expenses last month?"""
    basic_salary = 1250
    commission_rate = 0.10
    total_sales = 23600
    commission_earned = total_sales * commission_rate
    total_earnings = basic_salary + commission_earned
    savings = total_earnings * 0.20
    expenses = total_earnings - savings
    result = expenses
    return result

print(solution())