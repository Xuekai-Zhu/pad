def solution():
    distance = 150
    time = 2
    speed_limit = 60

    # Calculate the average speed John was driving
    average_speed = distance / time

    # Calculate how many mph above the speed limit John was driving
    mph_above_speed_limit = average_speed - speed_limit
    result = mph_above_speed_limit
    return result

print(solution())