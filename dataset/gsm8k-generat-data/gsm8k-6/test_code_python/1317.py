def solution():
    # Calculate how long it takes Diego to run the full block
    diego_time = 2.5 * 2  # Diego runs half the block in 2.5 minutes, so it would take him 2.5*2=5 minutes to run the full block
    # Calculate the average time in seconds for both racers
    average_time = ((3 * 60) + diego_time) / 2  # convert Carlos' time to seconds, add Diego's time in seconds, and divide by 2 for the average time
    result = average_time
    return result

print(solution())