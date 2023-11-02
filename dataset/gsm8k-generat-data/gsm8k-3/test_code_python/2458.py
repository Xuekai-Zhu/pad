def solution():
    """Robert, a sales agent, earns a basic salary of $1250 per month and,  10% commission on his monthly sales. Last month, his total sales were $23600. He allocated 20% of his total earnings to savings and the rest of the money to his monthly expenses. How much were his monthly expenses last month?"""
    # Define Robert's basic salary and commission rate
    BASIC_SALARY = 1250
    COMMISSION_RATE = 0.1

    # Get Robert's total earnings
    total_earnings = BASIC_SALARY + (COMMISSION_RATE * 23600)

    # Allocate 20% of his total earnings to savings
    savings = 0.2 * total_earnings

    # Calculate Robert's monthly expenses
    expenses = total_earnings - savings

    # Display Robert's monthly expenses
    result = expenses
    return result

print(solution())