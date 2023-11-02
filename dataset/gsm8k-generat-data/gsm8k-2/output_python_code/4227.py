def solution():
    """Martha receives a daily allowance of $12. She decides to save half of this amount every day. In the first week she kept her commitment with the exception of one day when she saved only a quarter of this amount. How much has she saved at the end of this week?"""
    daily_allowance = 12
    saved_percent = 0.5
    saved_amount = 0
    for i in range(1, 8):
        if i == 4:
            saved_amount += daily_allowance * 0.25
        else:
            saved_amount += daily_allowance * saved_percent

    result = saved_amount
    return result

print(solution())