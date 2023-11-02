def solution():
    fred_start = 212
    jane_received = 307
    charles_given = 156

    fred_total = fred_start + jane_received
    fred_left = fred_total - charles_given
    result = fred_left
    return result

print(solution())