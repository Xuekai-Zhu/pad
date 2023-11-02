def solution():
    sapling_spears = 3  # Marcy can make 3 spears out of a sapling
    log_spears = 9  # Marcy can make 9 spears out of a log
    num_saplings = 6  # Marcy has 6 saplings
    num_log = 1  # Marcy has 1 log

    # Calculate the total number of spears Marcy can make
    total_spears = (sapling_spears * num_saplings) + (log_spears * num_log)
    result = total_spears
    return result

print(solution())