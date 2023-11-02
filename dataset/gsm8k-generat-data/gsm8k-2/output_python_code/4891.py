def solution():
    """Liam wants to go to Paris, but first, he has to pay his bills. His trip costs $7,000, and his bills cost $3,500. Knowing that Liam has saved $500/month for 2 years, how much money will he have left after paying his bills?"""
    saved_per_month = 500
    total_saved = saved_per_month * 24
    total_expenses = 7000 + 3500
    remaining_money = total_saved - total_expenses
    result = remaining_money
    return result

print(solution())