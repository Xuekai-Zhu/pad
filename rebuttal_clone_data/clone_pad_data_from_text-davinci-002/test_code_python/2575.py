def solution():
    journey_miles = 35
    portions = 5
    speed_mph = 40
    time = 0.7
    portions_traveled = (time * speed_mph) / journey_miles
    result = portions_traveled
    return result

print(solution())