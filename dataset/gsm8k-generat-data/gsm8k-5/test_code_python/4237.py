def solution():
    total_distance = 74.5  # Total length of the race is 74.5 kilometers
    first_part_distance = 15.5  # First part is 15.5 kilometers long
    second_part_distance = 21.5  # Second part is 21.5 kilometers long
    third_part_distance = 21.5  # Third part is also 21.5 kilometers long

    # Calculate the remaining distance after the first three parts
    remaining_distance = total_distance - (first_part_distance + second_part_distance + third_part_distance)

    result = remaining_distance
    return result

print(solution())