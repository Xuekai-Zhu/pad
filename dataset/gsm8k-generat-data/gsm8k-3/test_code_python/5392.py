def solution():
    """Marcy can make 3 spears out of a sapling and 9 spears out of a log. How many spears can she make out of 6 saplings and a log?"""
    # Define the number of spears Marcy can make out of a sapling and a log
    SAPLING_SPEARS = 3
    LOG_SPEARS = 9

    # Define the number of saplings and logs Marcy has
    saplings = 6
    logs = 1

    # Calculate the total number of spears Marcy can make
    total_spears = (saplings * SAPLING_SPEARS) + (logs * LOG_SPEARS)

    # Display the total number of spears Marcy can make
    result = total_spears
    return result

print(solution())