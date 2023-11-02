def solution():
    total_woodblocks_needed = 80
    woodblocks_per_log = 5
    num_logs_available = 8

    # Calculate the total number of woodblocks that can be made from the available logs
    total_woodblocks_available = num_logs_available * woodblocks_per_log

    # Calculate the number of logs the carpenter still needs
    num_logs_needed = (total_woodblocks_needed - total_woodblocks_available) / woodblocks_per_log

    result = num_logs_needed
    return result

print(solution())