def solution():
    # Calculate the total amount paid by Jerry in the previous 2 months
    amount_paid = 12 + (12 + 3)  # Jerry paid $12 two months ago and $3 more last month
    remaining_debt = 50 - amount_paid  # Calculate the remaining debt Jerry has to pay
    result = remaining_debt
    return result

print(solution())