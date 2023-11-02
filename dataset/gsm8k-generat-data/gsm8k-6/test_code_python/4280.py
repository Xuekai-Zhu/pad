def solution():
    total_monthly_earnings = 100  # assume Zilla earns $100
    rent_percentage = 7  # Zilla spends 7% of her monthly earnings on rent
    rent_cost = 133  # Zilla spends $133 on her rent

    # Calculate Zilla's monthly expenses and savings
    monthly_expenses = (rent_cost / rent_percentage) * 50  # half of the rent cost goes to other monthly expenses
    savings = total_monthly_earnings - rent_cost - monthly_expenses

    result = savings
    return result

print(solution())