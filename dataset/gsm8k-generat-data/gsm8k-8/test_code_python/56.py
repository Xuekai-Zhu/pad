def solution():
    total_time = 2 * 60  # Convert 2 hours to minutes
    first_part_time = 25
    second_part_time = 2 * first_part_time
    third_part_time = total_time - first_part_time - second_part_time
    result = third_part_time
    return result

print(solution())