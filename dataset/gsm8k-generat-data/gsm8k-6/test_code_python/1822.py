def solution():
    # Calculate the distance covered by the ship on the second day
    distance_second_day = 3 * 100  # the ship sails to the east three times as far as the distance as covered on the first day

    # Calculate the total distance covered in the first two days
    total_distance_first_two_days = 100 + distance_second_day

    # Calculate the total distance covered in the three days
    total_distance = total_distance_first_two_days + distance_second_day + 110  # the ship traveled further east for 110 more miles than the distance it covered on the second day
    result = total_distance
    return result

print(solution())