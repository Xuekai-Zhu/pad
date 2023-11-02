def solution():
    """Barney washes his kitchen towels once a week. He owns eighteen towels and uses two at a time that he changes to clean towels daily. He missed one week of laundry. How many days the following week will Barney not have clean towels?"""
    total_towels = 18
    used_towels_per_day = 2
    days_without_laundry = 7
    missed_week_towels = used_towels_per_day * 7
    remaining_towels = total_towels - missed_week_towels
    days_without_clean_towels = (remaining_towels / used_towels_per_day) * 2
    result = days_without_clean_towels
    return result

print(solution())