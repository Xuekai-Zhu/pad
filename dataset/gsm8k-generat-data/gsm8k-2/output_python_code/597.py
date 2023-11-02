def solution():
    """Federal guidelines recommend eating at least 2 cups of vegetables per day. From breakfast on Sunday to the end of the day on Thursday, Sarah has eaten 8 cups. How many cups per day does Sarah need to eat of her vegetables in order to meet her daily minimum requirement for the week?"""
    min_daily_veggies = 2
    total_veggies_consumed = 8
    remaining_veggies = min_daily_veggies * 7 - total_veggies_consumed
    days_left_in_week = 7 - 5  
    cups_per_day = remaining_veggies / days_left_in_week
    result = cups_per_day
    return result

print(solution())