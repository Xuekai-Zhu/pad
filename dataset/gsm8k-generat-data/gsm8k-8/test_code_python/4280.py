def solution():
    # Define Zilla's monthly earnings and rent cost
    monthly_earnings = 0
    rent_cost = 133

    # Calculate Zilla's total spending on rent and other expenses
    total_spending = rent_cost / 0.07
    other_expenses = total_spending / 2

    # Calculate Zilla's monthly savings deposit
    savings_deposit = monthly_earnings - rent_cost - other_expenses
    result = savings_deposit
    return result

print(solution())