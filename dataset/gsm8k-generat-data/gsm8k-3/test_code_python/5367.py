def solution():
    """Kate has to fill 52 balloons for the party. Each balloon holds 5 gallons of air. For the first 10 minutes, she can fill the balloons at a rate of 8 gallons of air per minute. For the next five minutes, she fills them at half that rate. After that, she fills the rest of the balloons at a rate of 2 gallons of air per minute. How many minutes will it take her to fill all of the balloons?"""
    # Define the total number of balloons and the air capacity of each balloon
    total_balloons = 52
    balloon_air_capacity = 5

    # Define the filling rates for each time interval
    rate1 = 8 # gallons per minute
    rate2 = 4 # gallons per minute
    rate3 = 2 # gallons per minute

    # Calculate the total time it will take to fill all balloons
    time1 = 10 # minutes
    time2 = 5 # minutes
    balloons_filled1 = rate1 * time1 # balloons filled in first 10 minutes
    balloons_filled2 = rate2 * time2 # balloons filled in next 5 minutes
    balloons_filled3 = total_balloons - balloons_filled1 - balloons_filled2 # balloons filled in remaining time
    time3 = balloons_filled3 * balloon_air_capacity / rate3 # time taken to fill remaining balloons
    total_time = time1 + time2 + time3

    # Display the total time
    result = total_time
    return result

print(solution())