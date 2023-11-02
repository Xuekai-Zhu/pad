def solution():
    time_walking = 0.5  # Half an hour spent walking twice a day
    time_feeding = 0.2  # A fifth of an hour spent feeding the dog

    # Calculate the total time Larry spends on his dog each day
    total_time = (time_walking * 2) + time_feeding
    minutes_per_day = total_time * 60
    result = minutes_per_day
    return result

print(solution())