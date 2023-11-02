def solution():
    """A carpenter is building a house. He needs 80 woodblocks to build it. If he has 8 logs that can make five woodblocks each, how many logs does the carpenter still need?"""
    woodblocks_needed = 80
    woodblocks_per_log = 5
    logs_available = 8
    woodblocks_available = woodblocks_per_log * logs_available
    woodblocks_remaining = woodblocks_needed - woodblocks_available
    logs_needed = (woodblocks_remaining + woodblocks_per_log - 1) // woodblocks_per_log
    result = logs_needed
    return result

print(solution())