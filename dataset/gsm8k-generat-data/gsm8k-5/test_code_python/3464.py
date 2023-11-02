def solution():
    distance_per_minute = 10  # Lisa walks 10 meters each minute
    minutes_per_day = 60  # Lisa walks for an hour each day
    days = 2  # Lisa wants to know how many meters she will walk in 2 days

    # Calculate the total distance Lisa will walk in 2 days
    total_distance = distance_per_minute * minutes_per_day * days
    result = total_distance
    return result

print(solution())