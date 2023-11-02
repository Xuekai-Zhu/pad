def solution():
    """Martha receives a daily allowance of $12. She decides to save half of this amount every day. In the first week she kept her commitment with the exception of one day when she saved only a quarter of this amount. How much has she saved at the end of this week?"""
    # Define the daily allowance and the amount to save
    daily_allowance = 12
    amount_to_save = daily_allowance / 2

    # Calculate the amount saved for the first 6 days
    amount_saved_week = amount_to_save * 6

    # Calculate the amount saved on the 7th day
    amount_saved_7th_day = amount_to_save / 4

    # Calculate the total amount saved for the week
    total_saved = amount_saved_week + amount_saved_7th_day

    # Display the total amount saved
    result = total_saved
    return result

print(solution())