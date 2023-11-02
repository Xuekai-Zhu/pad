def solution():
    # Define the conversion ratio of saplings to spears
    saplings_to_spears = 3

    # Define the conversion ratio of log to spears
    log_to_spears = 9

    # Calculate the total number of spears that can be made from 6 saplings
    sapling_spears = 6 * saplings_to_spears

    # Calculate the total number of spears that can be made from one log
    log_spears = log_to_spears

    # Calculate the total number of spears that can be made from 6 saplings and a log
    total_spears = sapling_spears + log_spears

    result = total_spears
    return result

print(solution())