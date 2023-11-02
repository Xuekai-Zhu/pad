def solution():
    """Zilla spent 7% of her monthly earnings on rent, half of it on her other monthly expenses, and put the rest in her savings. If she spent $133 on her rent, how much does she deposit into her savings account in a month?"""
    rent_spending = 133
    rent_percentage = 0.07
    monthly_earnings = rent_spending / rent_percentage
    other_expenses = monthly_earnings * 0.5
    savings = monthly_earnings - rent_spending - other_expenses
    result = savings
    return result

print(solution())