def solution():
    woodblocks_needed = 80  # The carpenter needs 80 woodblocks for the house
    woodblocks_per_log = 5  # Each log can make 5 woodblocks
    logs_available = 8  # The carpenter has 8 logs available

    # Calculate the number of woodblocks the carpenter can make with the available logs
    woodblocks_made = woodblocks_per_log * logs_available

    # Calculate the number of woodblocks the carpenter still needs to make
    woodblocks_needed_remaining = woodblocks_needed - woodblocks_made

    # Calculate the number of logs the carpenter still needs
    logs_needed = woodblocks_needed_remaining / woodblocks_per_log
    result = logs_needed
    return result

print(solution())