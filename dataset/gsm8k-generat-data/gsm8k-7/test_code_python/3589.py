def solution():
    distance = 200
    sail_1_size = 24
    sail_1_speed = 50
    sail_2_size = 12
    sail_2_speed = 20

    # Calculate the time it takes to travel the distance with the first sail
    time_sail_1 = distance / sail_1_speed

    # Calculate the time it takes to travel the distance with the second sail
    time_sail_2 = distance / sail_2_speed

    # Calculate the time difference between the two sails
    time_difference = time_sail_2 - time_sail_1
    result = time_difference
    return result

print(solution())