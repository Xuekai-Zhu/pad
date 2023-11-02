def solution():
    """John takes a pill every 6 hours. How many pills does he take a week?"""
    pills_per_day = 4
    days_per_week = 7
    total_pills = pills_per_day * 24 / 6 * days_per_week
    result = total_pills
    return result

print(solution())