def solution():
    """Zilla spent 7% of her monthly earnings on rent, half of it on her other monthly expenses, and put the rest in her savings. If she spent $133 on her rent, how much does she deposit into her savings account in a month?"""
    rent_spending = 0.07
    rent_amount = 133
    total_spending = rent_amount / rent_spending
    other_spending = total_spending / 2
    savings_amount = total_spending - rent_amount - other_spending
    result = savings_amount
    return result

print(solution())