def solution():
    capacity = 6 * 12  # convert capacity from feet to inches
    drained = 3  # inches of rain drained per day
    total_rain = 10 + 20 + 30  # inches of rain on the first 3 days

    # Calculate the amount of rain needed to overflow the area
    overflow = capacity - (drained * 3)

    # Calculate the minimum amount of rain on the fourth day to cause overflow
    fourth_day_rain = overflow - total_rain
    if fourth_day_rain < 0:
        fourth_day_rain = 0
    result = fourth_day_rain
    return result

print(solution())