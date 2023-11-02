def solution():
    # Calculate the earnings for the first day
    day1_kilos = 5
    day1_earnings = day1_kilos * 2

    # Calculate the earnings for the second day
    day2_kilos = day1_kilos + 5
    day2_earnings = day2_kilos * 2

    # Calculate the earnings for the third day
    day3_kilos = day2_kilos * 2
    day3_earnings = day3_kilos * 2

    # Calculate the total earnings for all three days
    total_earnings = day1_earnings + day2_earnings + day3_earnings
    result = total_earnings
    return result

print(solution())