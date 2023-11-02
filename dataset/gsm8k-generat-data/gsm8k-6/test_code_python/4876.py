def solution():
    # Calculate MegaCorp's total monthly earnings and subtract monthly expenses to get monthly profits
    monthly_earnings = 3000000 * 30 + 5000000 * 30  # MegaCorp earns $3,000,000/day from mining and $5,000,000/day from oil refining
    monthly_expenses = 30000000  # MegaCorp's monthly expenses
    monthly_profits = monthly_earnings - monthly_expenses
    
    # Calculate MegaCorp's fine as 1% of its annual profits (12 times monthly profits)
    fine = 0.01 * 12 * monthly_profits
    result = fine
    return result

print(solution())