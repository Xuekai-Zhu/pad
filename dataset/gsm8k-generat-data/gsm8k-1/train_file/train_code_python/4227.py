def solution():
    """Martha receives a daily allowance of $12. She decides to save half of this amount every day. In the first week she kept her commitment with the exception of one day when she saved only a quarter of this amount. How much has she saved at the end of this week?"""
    daily_allowance = 12
    days_in_week = 7
    savings = 0
    for day in range(1, days_in_week+1):
        if day == 4: # On the fourth day, she saved only a quarter of her daily allowance
            savings += daily_allowance * 0.25
        else:
            savings += daily_allowance * 0.5
    result = savings
    return result

print(solution())