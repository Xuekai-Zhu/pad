def solution():
    # Calculate the total gallons of runoff that can be handled before the sewers overflow
    total_gallons = 240000  # gallons of runoff the sewers can handle
    gallons_per_day = 24 * 1000  # gallons of runoff produced by a day of rain
    days_of_rain = total_gallons // gallons_per_day  # number of days of rain the sewers can handle
    result = days_of_rain
    return result

print(solution())