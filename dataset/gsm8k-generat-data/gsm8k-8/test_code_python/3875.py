def solution():
    # Calculate the distance each snail covered
    distance_first_snail = 2 * 20
    distance_second_snail = 4 * 20
    distance_third_snail = 20 * 5 * 20

    # Calculate the time each snail took to cover the distance
    time_first_snail = 20
    time_second_snail = distance_second_snail / (2 * 20)
    time_third_snail = distance_third_snail / (5 * 20)

    result = time_third_snail
    return result

print(solution())