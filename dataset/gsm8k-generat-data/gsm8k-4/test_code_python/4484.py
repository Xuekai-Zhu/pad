def solution():
    """Each month, Diego deposits his $5,000 paycheck into a bank account, which he then uses for all of his expenses, which amount to $4,600 per month. How much, in dollars, does Diego save over the course of a year?"""
    # Define the monthly income and expenses
    monthly_income = 5000
    monthly_expenses = 4600

    # Calculate the monthly savings
    monthly_savings = monthly_income - monthly_expenses

    # Calculate the yearly savings
    yearly_savings = monthly_savings * 12

    result = yearly_savings
    return result

print(solution())