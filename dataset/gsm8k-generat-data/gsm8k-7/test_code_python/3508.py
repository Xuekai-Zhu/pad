def solution():
    morning_time = 1
    evening_time = 1.5
    morning_speed = 30

    # Calculate the distance that Mr. Maxwell drives to work
    morning_distance = morning_speed * morning_time

    # Calculate the speed that Mr. Maxwell needs to drive in the evening
    evening_speed = (morning_distance * 2) / evening_time

    result = evening_speed
    return result

print(solution())