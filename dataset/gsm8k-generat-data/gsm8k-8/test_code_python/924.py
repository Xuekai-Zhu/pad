def solution():
    # Calculate the total time for the wash cycle
    wash_time = 8 * 0.75  # 45 minutes per load = 0.75 hours per load

    # Calculate the total time for the dry cycle
    dry_time = 8  # 1 hour per load

    # Calculate the total time for both cycles
    total_time = wash_time + dry_time

    result = total_time
    return result

print(solution())