def solution():
    # Calculate the total number of woodblocks the carpenter can make with his logs
    total_woodblocks = 8 * 5

    # Calculate the number of woodblocks the carpenter still needs to make
    remaining_woodblocks = 80 - total_woodblocks

    # Calculate the number of logs the carpenter still needs
    remaining_logs = remaining_woodblocks / 5
    result = remaining_logs
    return result

print(solution())