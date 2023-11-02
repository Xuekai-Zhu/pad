def solution():
    """During my workout yesterday, I did 30 squats. Each day, I plan to increase my number of squats by 5 more than the previous day. If I do my workout for four consecutive days, how many squats will I perform the day after tomorrow?"""
    day_one_squats = 30
    increase_per_day = 5
    day_two_squats = day_one_squats + increase_per_day
    day_three_squats = day_two_squats + increase_per_day
    day_four_squats = day_three_squats + increase_per_day
    day_after_tomorrow_squats = day_three_squats + increase_per_day
    result = day_after_tomorrow_squats
    return result

print(solution())