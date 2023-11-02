def solution():
    """Ben starts each day with $50, spends $15 every day and saves the rest. After a few days, his mom doubled his total savings and his dad gave him an additional $10. If he now has $500, how many days have elapsed?"""
    initial_savings = 0
    daily_budget = 50
    daily_expenses = 15
    days_elapsed = 0
    while True:
        daily_savings = daily_budget - daily_expenses
        initial_savings += daily_savings
        if initial_savings >= 250:
            initial_savings *= 2
            initial_savings += 10
        if initial_savings == 500:
            break
        days_elapsed += 1
    result = days_elapsed
    return result

print(solution())