def solution():
    # Calculate the distance Stephen rides his bicycle to church
    distance_first_third = (16 / 60) * 15  # distance traveled during the first third of the trip
    distance_second_third = (12 / 60) * 15  # distance traveled during the second third of the trip
    distance_last_third = (20 / 60) * 15  # distance traveled during the last third of the trip
    total_distance = distance_first_third + distance_second_third + distance_last_third  # total distance traveled
    result = total_distance
    return result

print(solution())