def solution():
    first_snail_speed = 2
    second_snail_speed = 2 * first_snail_speed
    third_snail_speed = 5 * second_snail_speed
    first_snail_time = 20

    # Calculate the distance all snails traveled, assuming the same distance
    distance = first_snail_speed * first_snail_time

    # Calculate the time it took for the third snail to travel the same distance
    third_snail_time = distance / third_snail_speed
    result = third_snail_time
    return result

print(solution())