def solution():
    """Each month, Diego deposits his $5,000 paycheck into a bank account, which he then uses for all of his expenses, which amount to $4,600 per month. How much, in dollars, does Diego save over the course of a year?"""
    # Define Diego's monthly income and expenses
    monthly_income = 5000
    monthly_expenses = 4600

    # Calculate Diego's monthly savings
    monthly_savings = monthly_income - monthly_expenses

    # Calculate Diego's yearly savings
    yearly_savings = monthly_savings * 12

    # Display Diego's yearly savings
    result = yearly_savings
    return result

print(solution())