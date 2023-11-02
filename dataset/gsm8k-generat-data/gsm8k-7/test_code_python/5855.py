def solution():
    remaining_gummy_worms = 4
    days_passed = 4

    # Calculate the number of gummy worms Carlos had on day 3
    gummy_worms_day3 = remaining_gummy_worms * 2

    # Calculate the number of gummy worms Carlos had on day 2
    gummy_worms_day2 = gummy_worms_day3 * 2

    # Calculate the number of gummy worms Carlos had on day 1
    gummy_worms_day1 = gummy_worms_day2 * 2

    # Calculate the number of gummy worms Carlos had on day 0
    gummy_worms_day0 = gummy_worms_day1 * 2

    # Calculate the total number of gummy worms in the bag
    total_gummy_worms = gummy_worms_day0
    result = total_gummy_worms
    return result

print(solution())