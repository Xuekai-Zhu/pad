def solution():
    """Marcy can make 3 spears out of a sapling and 9 spears out of a log. How many spears can she make out of 6 saplings and a log?"""
    # Define the number of spears that can be made from a sapling and a log
    SPEARS_PER_SAPLING = 3
    SPEARS_PER_LOG = 9

    # Define the number of saplings and logs
    saplings = 6
    log = 1

    # Calculate the total number of spears that can be made
    total_spears = (saplings * SPEARS_PER_SAPLING) + (log * SPEARS_PER_LOG)

    result = total_spears
    return result

print(solution())