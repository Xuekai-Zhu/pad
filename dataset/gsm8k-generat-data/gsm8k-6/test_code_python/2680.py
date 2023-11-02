def solution():
    # Calculate the time it took James to find the first artifact
    find_1_time = 6/12 + 2  # 6 months of research and 2 years of expedition

    # Calculate the time it took James to find the second artifact
    find_2_time = 3 * find_1_time

    # Calculate the total time it took James to find both artifacts
    total_time = find_1_time + find_2_time
    result = total_time
    return result

print(solution())