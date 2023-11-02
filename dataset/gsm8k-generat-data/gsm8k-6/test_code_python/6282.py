def solution():
    # Calculate the amount of rain on each of the first three days
    day1 = 10  # inches of rain on day 1
    day2 = 2 * day1  # inches of rain on day 2
    day3 = 1.5 * day2  # inches of rain on day 3

    # Calculate the total amount of rain in the first three days
    total_rain = day1 + day2 + day3  # inches of rain in the first three days

    # Calculate the amount of rain that the area can still hold without overflowing
    available_capacity = (6 * 12) - (total_rain / 4) - (3 * 4)  # available capacity in inches

    # Calculate the minimum amount of rain on the fourth day to cause overflow
    minimum_rain_day4 = available_capacity + (3 * 12)  # in inches
    result = minimum_rain_day4
    return result

print(solution())