def solution():
    """Marcy can make 3 spears out of a sapling and 9 spears out of a log. How many spears can she make out of 6 saplings and a log?"""
    sapling_spears = 3
    log_spears = 9
    six_saplings_spears = 6 * sapling_spears
    one_log_spears = log_spears
    total_spears = six_saplings_spears + one_log_spears
    result = total_spears
    return result

print(solution())