def solution():
    total_time = 2 * 60  # Leo had 2 hours to finish his assignment, which is 120 minutes
    time_part_1 = 25  # Leo finished the first part in 25 minutes
    time_part_2 = 2 * time_part_1  # It took Leo twice as long to finish the second part
    time_part_3 = total_time - time_part_1 - time_part_2  # The remaining time is for the third part

    result = time_part_3
    return result

print(solution())