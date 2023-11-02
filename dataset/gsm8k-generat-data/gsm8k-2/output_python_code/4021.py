def solution():
    """James spends 30 minutes twice a day on meditation. How many hours a week does he spend meditating?"""
    minutes_per_day = 30 * 2
    hours_per_day = minutes_per_day / 60
    hours_per_week = hours_per_day * 7
    result = hours_per_week
    return result

print(solution())