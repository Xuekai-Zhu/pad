def solution():
    total_debt = 50  # Jerry's total debt is $50
    paid_two_months_ago = 12  # Jerry paid $12 two months ago
    paid_last_month = 15  # Jerry paid $3 more last month

    # Calculate the remaining debt
    remaining_debt = total_debt - paid_two_months_ago - paid_last_month
    result = remaining_debt
    return result

print(solution())