def solution():
    """Mr. Isaac rides his bicycle at the rate of 10 miles per hour for 30 minutes. If he rides for another 15 miles, rests for 30 minutes, and then covers the remaining distance of 20 miles, what's the total time in minutes took to travel the whole journey?"""
    speed_mph = 10
    time_1 = 0.5 # 30 minutes in hours
    distance_1 = speed_mph * time_1
    distance_2 = 15
    time_rest = 0.5 # 30 minutes in hours
    distance_3 = 20
    total_time = ((distance_1 + distance_2 + distance_3) / speed_mph) + time_rest
    result = total_time * 60 # convert hours to minutes
    return result

print(solution())