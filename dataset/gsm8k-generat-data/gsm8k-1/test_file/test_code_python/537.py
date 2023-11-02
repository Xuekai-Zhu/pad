def solution():
    """Elvis has a monthly saving target of $1125. In April, he wants to save twice as much daily in the second half as he saves in the first half in order to hit his target. How much does he have to save for each day in the second half of the month?"""
    target_savings = 1125
    days_in_month = 30
    first_half_days = days_in_month // 2
    second_half_days = days_in_month - first_half_days
    first_half_savings = target_savings / 2 / first_half_days
    second_half_savings = target_savings / 2 / second_half_days
    result = second_half_savings
    return result

print(solution())