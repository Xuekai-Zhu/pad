def solution():
    """Federal guidelines recommend eating at least 2 cups of vegetables per day. From breakfast on Sunday to the end of the day on Thursday, Sarah has eaten 8 cups. How many cups per day does Sarah need to eat of her vegetables in order to meet her daily minimum requirement for the week?"""
    recommended_daily_veggie_intake = 2
    current_veggie_intake = 8
    days_left_in_week = 7 - 5 # 5 represents the number of days already passed (Sunday to Thursday)
    cups_left_to_meet_recommendation = recommended_daily_veggie_intake * days_left_in_week - current_veggie_intake
    cups_per_day_needed = cups_left_to_meet_recommendation / days_left_in_week
    result = cups_per_day_needed
    
    return result

print(solution())