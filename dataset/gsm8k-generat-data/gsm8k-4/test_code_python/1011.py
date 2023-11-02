def solution():
    """A carpenter is building a house. He needs 80 woodblocks to build it. If he has 8 logs that can make five woodblocks each, how many logs does the carpenter still need?"""
    # Define the total number of woodblocks needed to build the house
    total_woodblocks = 80

    # Define the number of woodblocks that can be made from one log
    woodblocks_per_log = 5

    # Calculate the number of woodblocks the carpenter already has
    woodblocks_on_hand = 8 * woodblocks_per_log

    # Calculate the number of woodblocks the carpenter still needs
    woodblocks_needed = total_woodblocks - woodblocks_on_hand

    # Calculate the number of logs the carpenter still needs
    logs_needed = woodblocks_needed / woodblocks_per_log

    # Round up to the nearest whole number of logs
    logs_needed = math.ceil(logs_needed)

    # return the result
    result = logs_needed
    return result

print(solution())