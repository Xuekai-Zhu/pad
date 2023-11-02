def solution():
    """Kate has to fill 52 balloons for the party. Each balloon holds 5 gallons of air. For the first 10 minutes, she can fill the balloons at a rate of 8 gallons of air per minute. For the next five minutes, she fills them at half that rate. After that, she fills the rest of the balloons at a rate of 2 gallons of air per minute. How many minutes will it take her to fill all of the balloons?"""
    balloons = 52
    gallons_per_balloon = 5
    rate_1 = 8
    rate_2 = rate_1 / 2
    rate_3 = 2
    time_1 = 10
    time_2 = 5
    time_3 = (balloons * gallons_per_balloon - (rate_1 * time_1 + rate_2 * time_2)) / rate_3
    total_time = time_1 + time_2 + time_3
    result = total_time
    return result

print(solution())