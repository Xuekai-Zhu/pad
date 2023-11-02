def solution():
    """Tim spends 1 hour a day meditating. He spends twice as much time reading. How much time a week does he spend reading?"""
    meditate_time_per_day = 1
    read_time_per_day = meditate_time_per_day * 2
    days_per_week = 7
    total_reading_time = read_time_per_day * days_per_week
    result = total_reading_time
    return result

print(solution())