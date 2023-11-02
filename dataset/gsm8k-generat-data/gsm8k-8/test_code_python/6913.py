def solution():
    # Calculate the number of gumballs Kim gets each day
    day1_gumballs = 9 * 3
    day2_gumballs = 9 * 6
    day3_gumballs = 9 * 5

    # Calculate the total number of gumballs Kim gets
    total_gumballs = day1_gumballs + day2_gumballs + day3_gumballs

    # Calculate the number of days the gumballs will last
    days = total_gumballs // 3
    result = days
    return result

print(solution())