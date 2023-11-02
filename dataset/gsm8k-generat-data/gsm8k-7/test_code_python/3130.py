def solution():
    speed = 60
    time_one = 4
    time_two = 9
    break_time = 0.5  # in hours

    # Calculate the distance traveled during the first leg of the trip
    distance_one = speed * time_one

    # Calculate the distance traveled during the second leg of the trip
    distance_two = speed * time_two

    # Calculate the total distance traveled
    total_distance = distance_one + distance_two

    # Subtract the distance traveled during the break
    total_distance -= (speed * break_time)

    result = total_distance
    return result

print(solution())