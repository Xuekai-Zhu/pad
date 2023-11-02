def solution():
    # Calculate Greta's earnings
    greta_earnings = 40 * 12

    # Calculate Lisa's earnings per hour to match Greta's earnings
    lisa_hourly_rate = greta_earnings / 40

    # Calculate the number of hours Lisa would have to work
    lisa_hours = greta_earnings / (15 * lisa_hourly_rate)
    result = lisa_hours
    return result

print(solution())