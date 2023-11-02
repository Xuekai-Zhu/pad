def solution():
    # Calculate the number of gumballs Kim gets on the first day
    gumballs_first_day = 9 * 3  # 9 gumballs for each pair of earrings, and Kim brings 3 pairs of earrings

    # Calculate the number of gumballs Kim gets on the second day
    gumballs_second_day = 9 * 2 * 3  # 9 gumballs for each pair of earrings, and Kim brings twice as many as on the first day

    # Calculate the number of gumballs Kim gets on the third day
    gumballs_third_day = 9 * (2*3 - 1)  # 9 gumballs for each pair of earrings, and Kim brings 1 less than on the second day

    # Calculate the total number of gumballs Kim gets
    total_gumballs = gumballs_first_day + gumballs_second_day + gumballs_third_day

    # Calculate the number of days the gumballs will last
    days_last = total_gumballs // 3  # Kim eats 3 gumballs a day

    result = days_last
    return result

print(solution())