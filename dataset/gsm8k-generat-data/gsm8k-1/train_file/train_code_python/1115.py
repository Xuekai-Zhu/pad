def solution():
    """Ben starts each day with $50, spends $15 every day and saves the rest. After a few days, his mom doubled his total savings and his dad gave him an additional $10. If he now has $500, How many days have elapsed?"""
    starting_amount = 50
    daily_spending = 15
    mom_multiplier = 2
    extra_money = 10
    current_total = starting_amount
    days_elapsed = 0
    while current_total < 500:
        days_elapsed += 1
        current_total -= daily_spending
        current_total += (starting_amount - daily_spending)
        current_total *= mom_multiplier
        current_total += extra_money
    result = days_elapsed
    return result

print(solution())