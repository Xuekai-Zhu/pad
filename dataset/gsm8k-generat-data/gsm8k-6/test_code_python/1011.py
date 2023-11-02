def solution():
    # Calculate the total number of woodblocks the carpenter can make with the available logs
    total_woodblocks = 8 * 5  # 8 logs that can make five woodblocks each

    # Calculate the number of logs the carpenter still needs
    logs_needed = 80 - total_woodblocks
    result = logs_needed
    return result

print(solution())