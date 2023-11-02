def solution():
    # Calculate the total amount of air needed to fill all 52 balloons
    total_air = 52 * 5  # each balloon holds 5 gallons of air

    # Calculate the amount of air Kate fills in the first 10 minutes
    air_filled_10min = 8 * 10  # she fills at a rate of 8 gallons per minute

    # Calculate the amount of air Kate fills in the next 5 minutes
    air_filled_5min = 4 * 5  # she fills at half the rate of 8 gallons per minute

    # Calculate the remaining amount of air Kate needs to fill after the first 15 minutes
    remaining_air = total_air - air_filled_10min - air_filled_5min

    # Calculate the time it takes Kate to fill the rest of the balloons at a rate of 2 gallons per minute
    time = remaining_air / 2  # she fills at a rate of 2 gallons per minute

    # Calculate the total time it takes Kate to fill all of the balloons
    total_time = 10 + 5 + time  # first 10 minutes at 8 gallons per minute, next 5 minutes at 4 gallons per minute, remaining time at 2 gallons per minute

    result = total_time
    return result

print(solution())