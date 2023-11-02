def solution():
    """James takes up dancing for fitness. He loses twice as many calories per hour as he did when he was walking. He dances twice a day for .5 hours each time and he does this 4 times a week. He burned 300 calories an hour walking. How many calories does he lose a week from dancing?"""
    walking_calories_per_hour = 300
    dancing_calories_per_hour = walking_calories_per_hour * 2
    daily_dancing_calories_lost = dancing_calories_per_hour * 0.5 * 2
    total_dancing_calories_lost_per_week = daily_dancing_calories_lost * 4
    result = total_dancing_calories_lost_per_week
    return result

print(solution())