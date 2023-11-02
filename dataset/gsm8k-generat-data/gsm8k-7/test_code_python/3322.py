def solution():
    num_coasters = 5
    first_speed = 50
    second_speed = 62
    third_speed = 73
    fourth_speed = 70
    average_speed = 59

    # Calculate the total distance covered on the first four coasters
    total_distance_covered = (num_coasters - 1) * average_speed

    # Calculate the total distance covered on the first four coasters
    total_distance_covered -= (first_speed + second_speed + third_speed + fourth_speed)

    # Calculate the speed of the fifth coaster
    fifth_speed = (total_distance_covered / num_coasters) + average_speed

    result = fifth_speed
    return result

print(solution())