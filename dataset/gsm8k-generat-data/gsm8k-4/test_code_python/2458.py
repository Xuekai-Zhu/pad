def solution():
    """Robert, a sales agent, earns a basic salary of $1250 per month and,  10% commission on his monthly sales. Last month, his total sales were $23600. He allocated 20% of his total earnings to savings and the rest of the money to his monthly expenses. How much were his monthly expenses last month?"""
    # Define the basic salary and commission rate
    basic_salary = 1250
    commission_rate = 0.1

    # Calculate the commission earned from sales
    sales = 23600
    commission = sales * commission_rate

    # Calculate the total earnings
    total_earnings = basic_salary + commission

    # Calculate the amount saved
    savings = total_earnings * 0.2

    # Calculate the monthly expenses
    expenses = total_earnings - savings

    result = expenses
    return result

print(solution())