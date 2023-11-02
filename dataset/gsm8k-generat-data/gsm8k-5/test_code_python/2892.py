def solution():
    distance = 150  # John travels 150 miles
    time = 2  # John takes 2 hours to travel 150 miles
    speed_limit = 60  # The speed limit is 60 mph

    # Calculate the speed John was driving
    actual_speed = distance / time

    # Calculate how many mph above the speed limit John was driving
    mph_above_speed_limit = actual_speed - speed_limit
    result = mph_above_speed_limit
    return result

print(solution())