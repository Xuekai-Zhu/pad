def solution():
    """Barney washes his kitchen towels once a week. He owns eighteen towels and uses two at a time that he changes to clean towels daily. He missed one week of laundry. How many days the following week will Barney not have clean towels?"""
    towels_owned = 18
    towels_used_per_day = 2
    days_per_week = 7
    missing_week = 1
    total_towels_used = (days_per_week * towels_used_per_day * (missing_week + 1)) - (towels_owned * (missing_week + 1))
    days_without_clean_towels = total_towels_used - towels_owned
    result = days_without_clean_towels
    return result

print(solution())