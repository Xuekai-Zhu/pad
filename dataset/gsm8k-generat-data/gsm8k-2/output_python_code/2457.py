def solution():
    """Robert, a sales agent, earns a basic salary of $1250 per month and, 10% commission on his monthly sales. Last month, his total sales were $23600. He allocated 20% of his total earnings to savings and the rest of the money to his monthly expenses. How much were his monthly expenses last month?"""
    basic_salary = 1250
    commission_rate = 0.1
    total_sales = 23600
    commission = commission_rate * total_sales
    total_earnings = basic_salary + commission
    savings = 0.2 * total_earnings
    expenses = total_earnings - savings
    result = expenses
    return result

print(solution())