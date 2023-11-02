def solution():
    gumballs_per_earring = 9
    earrings1 = 3
    earrings2 = earrings1 * 2
    earrings3 = earrings2 - 1
    gumballs_per_day = 3

    # Calculate the total number of gumballs Kim will get for all her earrings
    total_gumballs = (earrings1 + earrings2 + earrings3) * gumballs_per_earring

    # Calculate the number of days the gumballs will last
    num_days = total_gumballs / gumballs_per_day
    result = num_days
    return result

print(solution())