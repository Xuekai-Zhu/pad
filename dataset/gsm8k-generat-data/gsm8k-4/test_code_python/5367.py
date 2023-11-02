def solution():
    """Kate has to fill 52 balloons for the party. Each balloon holds 5 gallons of air. For the first 10 minutes, she can fill the balloons at a rate of 8 gallons of air per minute. For the next five minutes, she fills them at half that rate. After that, she fills the rest of the balloons at a rate of 2 gallons of air per minute. How many minutes will it take her to fill all of the balloons?"""
    # Define the number of balloons to fill and the amount of air each balloon holds
    total_balloons = 52
    balloon_capacity = 5

    # Calculate the total amount of air needed to fill all the balloons
    total_air = total_balloons * balloon_capacity

    # Calculate the amount of air filled in the first 10 minutes
    air_filled_10min = 8 * 10 * total_balloons

    # Calculate the amount of air filled in the next 5 minutes at half the rate
    air_filled_5min = 4 * 5 * total_balloons

    # Calculate the amount of air left to fill after the first 15 minutes
    air_left = total_air - air_filled_10min - air_filled_5min

    # Calculate the time needed to fill the remaining air at a rate of 2 gallons per minute
    time_left = air_left / 2

    # Calculate the total time needed to fill all the balloons
    total_time = 10 + 5 + time_left

    # return the result
    result = total_time
    return result

print(solution())