def solution():
    # Calculate the total number of gumballs Kim gets on the first day
    gumballs_day1 = 9 * 3  # 9 gumballs for each of the 3 pairs of earrings

    # Calculate the total number of gumballs Kim gets on the second day
    gumballs_day2 = 9 * 2 * 6  # 9 gumballs for each of the twice as many (6) pairs of earrings

    # Calculate the total number of gumballs Kim gets on the third day
    gumballs_day3 = 9 * (2 * 6 - 1)  # 9 gumballs for each of 1 less than (2*6) pairs of earrings

    # Calculate the total number of gumballs Kim has
    total_gumballs = gumballs_day1 + gumballs_day2 + gumballs_day3

    # Calculate the number of days the gumballs will last
    days_last = total_gumballs // 3  # Kim eats 3 gumballs a day

    result = days_last
    return result

print(solution())