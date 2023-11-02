def solution():
    # Calculate the number of beats per hour
    beats_per_hour = 200 * 60

    # Calculate the total number of beats James hears in one day
    beats_per_day = beats_per_hour * 2

    # Calculate the total number of beats James hears in one week
    beats_per_week = beats_per_day * 7
    result = beats_per_week
    return result

print(solution())