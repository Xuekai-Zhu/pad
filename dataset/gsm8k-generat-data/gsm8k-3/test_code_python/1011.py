def solution():
    """A carpenter is building a house. He needs 80 woodblocks to build it. If he has 8 logs that can make five woodblocks each, how many logs does the carpenter still need?"""
    # Define the number of woodblocks needed to build the house
    woodblocks_needed = 80

    # Define the number of woodblocks that can be made from each log
    woodblocks_per_log = 5

    # Calculate the total number of woodblocks that can be made from the logs
    woodblocks_from_logs = 8 * woodblocks_per_log

    # Calculate the number of logs still needed to make the remaining woodblocks
    logs_needed = (woodblocks_needed - woodblocks_from_logs) / woodblocks_per_log

    # Round up to the nearest whole number of logs
    logs_needed = math.ceil(logs_needed)

    # Display the number of logs needed
    result = logs_needed
    return result

print(solution())