def solution():
    """James takes up dancing for fitness. He loses twice as many calories per hour as he did when he was walking. He dances twice a day for .5 hours each time and he does this 4 times a week. He burned 300 calories an hour walking. How many calories does he lose a week from dancing?"""
    walking_calories_per_hour = 300
    dancing_calories_per_hour = 2 * walking_calories_per_hour
    dancing_time_per_day = 1
    dancing_time_per_week = 4 * dancing_time_per_day
    total_calories_lost_per_day = (dancing_calories_per_hour * dancing_time_per_day) * 2
    total_calories_lost_per_week = total_calories_lost_per_day * dancing_time_per_week
    result = total_calories_lost_per_week
    return result

print(solution())