def solution():
    """Mr. Isaac rides his bicycle at the rate of 10 miles per hour for 30 minutes. If he rides for another 15 miles, rests for 30 minutes, and then covers the remaining distance of 20 miles, what's the total time in minutes took to travel the whole journey?"""
    speed = 10 # mph
    time_first_leg = 0.5 # in hours
    distance_first_leg = speed * time_first_leg # in miles
    distance_second_leg = 15 # in miles
    rest_time = 0.5 # in hours
    distance_third_leg = 20 # in miles
    total_distance = distance_first_leg + distance_second_leg + distance_third_leg
    total_time = time_first_leg + rest_time + (distance_third_leg / speed)
    result = total_time * 60 # converting to minutes
    return result

print(solution())