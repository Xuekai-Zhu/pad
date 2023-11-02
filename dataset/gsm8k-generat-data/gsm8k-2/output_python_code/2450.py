def solution():
    """Sanya can wash 7 bath towels in one wash, which will take 1 hour. She only has 2 hours in a day to do this task. If she has 98 bath towels, how many days will she need to wash all of them?"""
    towels_per_wash = 7
    wash_time = 1
    daily_time = 2
    total_towels = 98
    towels_washed_per_day = int((daily_time / wash_time) * towels_per_wash)
    total_days = int(total_towels / towels_washed_per_day)
    if total_towels % towels_washed_per_day != 0:
        total_days += 1
    result = total_days
    return result

print(solution())