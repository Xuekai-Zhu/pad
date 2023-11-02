def solution():
    """A carpenter is building a house. He needs 80 woodblocks to build it. If he has 8 logs that can make five woodblocks each, how many logs does the carpenter still need?"""
    woodblocks_per_log = 5
    total_woodblocks = 80
    available_logs = 8
    woodblocks_from_available_logs = available_logs * woodblocks_per_log
    remaining_woodblocks = total_woodblocks - woodblocks_from_available_logs
    additional_logs_needed = (remaining_woodblocks + woodblocks_per_log - 1) // woodblocks_per_log
    result = additional_logs_needed
    return result

print(solution())