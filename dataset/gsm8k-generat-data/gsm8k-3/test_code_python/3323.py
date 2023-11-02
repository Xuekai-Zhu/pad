def solution():
    """Brad's car broke down on an isolated road.  At the time, Brad was traveling with Jim and Marcus.  So, the three decided to push the car back into town, which was 10 miles away.  For the first three miles, Brad steered as Jim and Marcus pushed at a speed of 6 miles per hour.  Then, for the next 3 miles, Jim steered, as Brad and Marcus pushed at a speed of 3 miles per hour.  For the last four miles, Marcus steered as Brad and Jim pushed at a speed of 8 miles per hour.  How long did it take, in hours, to push the car back to town?"""
    # Calculate the time it took for each leg of the journey
    time1 = 3 / 6
    time2 = 3 / 3
    time3 = 4 / 8

    # Calculate the total time taken to push the car back to town
    total_time = time1 + time2 + time3

    # Display the total time taken
    result = total_time
    return result

print(solution())