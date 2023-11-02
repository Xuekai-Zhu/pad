def solution():
    miles = 2.5
    minutes_per_mile = 20
    minutes_walked = 1 * minutes_per_mile
    minutes_left = miles * minutes_per_mile - minutes_walked
    result = minutes_left
    
    return result

print(solution())