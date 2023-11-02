def solution():
    # Calculate the number of beats James hears in one day
    beats_per_day = 200 * 60 * 2  # 200 beats per minute * 60 minutes * 2 hours

    # Calculate the number of beats James hears in one week
    beats_per_week = beats_per_day * 7

    result = beats_per_week
    return result

print(solution())