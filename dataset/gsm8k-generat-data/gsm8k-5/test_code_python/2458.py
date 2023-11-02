def solution():
    basic_salary = 1250  # Robert's basic salary is $1250 per month
    commission_rate = 0.1  # Robert earns 10% commission on his monthly sales
    total_sales = 23600  # Robert's total sales revenue last month was $23600

    # Calculate the commission earned by Robert
    commission = commission_rate * total_sales

    # Calculate Robert's total earnings
    total_earnings = basic_salary + commission

    # Calculate the amount of money Robert saved
    savings = 0.2 * total_earnings

    # Calculate Robert's monthly expenses
    monthly_expenses = total_earnings - savings
    result = monthly_expenses
    return result

print(solution())