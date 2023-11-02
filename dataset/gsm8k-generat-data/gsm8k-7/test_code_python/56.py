def solution():
    total_time = 2 * 60  # 2 hours in minutes

    # Calculate the time spent on the first part
    time_part_1 = 25

    # Calculate the time spent on the second part
    time_part_2 = 2 * time_part_1

    # Calculate the total time spent on the first two parts
    total_time_parts_1_and_2 = time_part_1 + time_part_2

    # Calculate the time spent on the third part
    time_part_3 = total_time - total_time_parts_1_and_2

    result = time_part_3
    return result

print(solution())