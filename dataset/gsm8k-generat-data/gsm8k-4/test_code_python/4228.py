def solution():
    """Martha receives a daily allowance of $12. She decides to save half of this amount every day. In the first week she kept her commitment with the exception of one day when she saved only a quarter of this amount. How much has she saved at the end of this week?"""
    # Define the daily allowance and the number of days in a week
    daily_allowance = 12
    days_in_week = 7

    # Calculate the total amount saved in the first 6 days
    total_saved = (daily_allowance / 2) * 6

    # Calculate the amount saved on the 7th day
    saved_on_7th_day = daily_allowance / 4

    # Calculate the total amount saved in the week
    total_saved += saved_on_7th_day

    result = total_saved
    return result

print(solution())