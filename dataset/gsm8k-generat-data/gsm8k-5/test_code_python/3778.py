def solution():
    current_length = 200  # The current length of the highway is 200 miles
    total_length = 650  # The total length of the highway will be 650 miles
    first_day_distance = 50  # 50 miles are built on the first day
    second_day_distance = 3 * first_day_distance  # Three times the distance built on the first day is built on the second day

    # Calculate the total distance built after two days
    total_distance_built = first_day_distance + second_day_distance

    # Calculate the distance still needed to finish the extension
    distance_remaining = total_length - current_length - total_distance_built
    result = distance_remaining
    return result

print(solution())