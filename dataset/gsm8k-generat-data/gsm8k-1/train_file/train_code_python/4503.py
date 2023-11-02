def solution():
    """An old car can drive 8 miles in one hour. After 5 hours of constant driving, the car needs to get cooled down which takes 1 hour. How many miles can this car drive in 13 hours?"""
    miles_per_hour = 8
    constant_driving_hours = 5
    cool_down_hours = 1
    total_driving_hours = 13
    total_driving_time = constant_driving_hours + cool_down_hours
    total_driving_distance = miles_per_hour * constant_driving_hours
    total_distance = total_driving_distance + (miles_per_hour * (total_driving_hours - total_driving_time))
    result = total_distance
    return result

print(solution())